"""Build the food vs non-food inflation chart for the 2026-07-15 Insights post.

Run from the repo root:

    python scripts/make_inflation_chart.py

Reads   ../Data/BOGnew.csv   (Bank of Ghana monthly series; kept outside the
                              repo on purpose — see .gitignore)
Writes  images/ghana-food-vs-nonfood-inflation.svg

Also prints every figure the post quotes, so the prose can be checked against
the data rather than trusted.

Palette note: the two series use categorical slots 1 (blue) and 2 (aqua),
validated against this site's actual surface (#fdfdfd, minima's background):
CVD deltaE 73.6, well clear. Aqua sits at 2.77:1 on that surface — below 3:1 —
so both series carry direct labels rather than relying on colour alone.
"""

import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(ROOT, os.pardir, "Data", "BOGnew.csv")
OUT = os.path.join(ROOT, "images", "ghana-food-vs-nonfood-inflation.svg")

SURFACE = "#fdfdfd"   # minima's $background-color
NONFOOD = "#2a78d6"   # categorical slot 1
FOOD    = "#1baf7a"   # categorical slot 2
INK     = "#0b0b0b"
SECOND  = "#52514e"
MUTED   = "#898781"
GRID    = "#e1e0d9"
AXIS    = "#c3c2b7"

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def load():
    raw = pd.read_csv(SRC)
    raw = raw.loc[:, ~raw.columns.str.startswith("Unnamed")]
    # The sheet carries ~236 empty trailing rows.
    raw = raw[raw["Variables"].notna()]
    # Year reads as float64 because of those rows, so it would stringify to
    # "2020.0" and never match %Y-%b.
    raw["Year"] = raw["Year"].astype("Int64")
    raw["Variables"] = raw["Variables"].str.strip()

    long = raw.melt(id_vars=["Year", "Variables"], value_vars=MONTHS,
                    var_name="Month", value_name="value")
    long["value"] = pd.to_numeric(
        long["value"].astype(str).str.replace(",", "", regex=False).str.strip(),
        errors="coerce")
    long["date"] = pd.to_datetime(long["Year"].astype(str) + "-" + long["Month"],
                                  format="%Y-%b", errors="coerce")
    long = long.dropna(subset=["date"]).sort_values("date")

    w = long.pivot_table(index="date", columns="Variables", values="value")
    food = w[[c for c in w.columns if "Food Inflation" in c][0]]
    nonf = w[[c for c in w.columns if "Non-Food" in c][0]]
    return pd.DataFrame({"food": food, "nonfood": nonf}).dropna()


def draw(d):
    plt.rcParams.update({
        "svg.fonttype": "none",   # keep text as text; inherits the page font
        "font.family": ["Segoe UI", "DejaVu Sans", "sans-serif"],
        "figure.facecolor": SURFACE,
        "axes.facecolor": SURFACE,
        "savefig.facecolor": SURFACE,
    })

    fig, ax = plt.subplots(figsize=(9.2, 5.0), dpi=170)
    ax.grid(True, axis="y", color=GRID, linewidth=0.8, zorder=0)
    ax.set_axisbelow(True)

    ax.plot(d.index, d["nonfood"], color=NONFOOD, linewidth=2, zorder=3)
    ax.plot(d.index, d["food"], color=FOOD, linewidth=2, zorder=3)

    last = d.index[-1]
    ax.annotate("Non-food", xy=(last, d["nonfood"].iloc[-1]),
                xytext=(8, 4), textcoords="offset points",
                color=NONFOOD, fontsize=11, fontweight="semibold", va="center")
    ax.annotate("Food", xy=(last, d["food"].iloc[-1]),
                xytext=(8, -2), textcoords="offset points",
                color=FOOD, fontsize=11, fontweight="semibold", va="center")

    # Label the month the arrow points at. The widest MONTHLY gap is Aug 2014
    # (18.9pp); the oft-quoted "2015, ~16pp" is the annual average and would not
    # match the arrow.
    peak = (d["nonfood"] - d["food"]).idxmax()
    ax.annotate("August 2014: non-food ran 18.9pp\nabove food — the widest gap on record",
                xy=(peak, d.loc[peak, "nonfood"]),
                xytext=(pd.Timestamp("2009-10-01"), 25.2), textcoords="data",
                fontsize=9.5, color=SECOND, ha="left", va="center",
                arrowprops=dict(arrowstyle="-", color=AXIS, linewidth=1,
                                connectionstyle="arc3,rad=0.18"))
    ax.scatter([peak], [d.loc[peak, "nonfood"]], s=34, color=NONFOOD,
               edgecolor=SURFACE, linewidth=2, zorder=4)

    # Annotate the widest 2020 gap, not the first crossing: food had already
    # edged above non-food in Jul 2007, Nov 2018 and three months of 2019, so
    # "first time" would be false. What is unprecedented is the size.
    gap = d["food"] - d["nonfood"]
    peak2020 = gap[gap.index.year == 2020].idxmax()
    ax.annotate("April–May 2020: food ran 6.7pp\nabove non-food — over four times\nany earlier gap",
                xy=(peak2020, d.loc[peak2020, "food"]),
                xytext=(pd.Timestamp("2017-04-01"), 21.5), textcoords="data",
                fontsize=9.5, color=SECOND, ha="left", va="center",
                arrowprops=dict(arrowstyle="-", color=AXIS, linewidth=1,
                                connectionstyle="arc3,rad=0.2"))
    ax.scatter([peak2020], [d.loc[peak2020, "food"]], s=34, color=FOOD,
               edgecolor=SURFACE, linewidth=2, zorder=4)

    ax.set_title("Food was Ghana's tame inflation component — until 2020",
                 fontsize=14, color=INK, loc="left", pad=36, fontweight="semibold")
    ax.text(0, 1.035, "Year-on-year inflation, monthly, Jan 2006 – Aug 2020",
            transform=ax.transAxes, fontsize=10, color=MUTED, va="bottom")

    ax.set_ylabel("Year-on-year inflation (%)", fontsize=10, color=SECOND)
    ax.yaxis.set_major_formatter(lambda v, p: "%d%%" % v)
    ax.xaxis.set_major_locator(mdates.YearLocator(2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.tick_params(colors=MUTED, labelsize=9.5, length=0)

    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(AXIS)
        ax.spines[side].set_linewidth(1)

    ax.set_xlim(d.index[0], d.index[-1] + pd.Timedelta(days=420))
    fig.text(0.005, -0.02, "Source: Bank of Ghana. Chart: Joseph Otoo.",
             fontsize=8.5, color=MUTED, ha="left")
    fig.tight_layout()

    try:
        fig.savefig(OUT, bbox_inches="tight", pad_inches=0.28)
        print("wrote", OUT)
    except (FileNotFoundError, PermissionError) as exc:
        # Windows Defender's Controlled Folder Access protects Documents\ and
        # blocks writes from apps that are not on its allow-list. python.exe is
        # not, so the write fails — and Windows reports it as FileNotFoundError
        # rather than a permission error, which sends you hunting for a missing
        # directory that is right there.
        import tempfile, os as _os
        fallback = _os.path.join(tempfile.gettempdir(),
                                 _os.path.basename(OUT))
        fig.savefig(fallback, bbox_inches="tight", pad_inches=0.28)
        print("could NOT write %s\n  (%s: %s)" % (OUT, type(exc).__name__, exc))
        print("\nThis is almost certainly Controlled Folder Access, not a bug:")
        print("  Windows Security > Virus & threat protection > Manage settings")
        print("  > Controlled folder access > Allow an app  ->  add python.exe")
        print("\nWrote it here instead — copy it into images/ with Explorer:")
        print(" ", fallback)


def report(d):
    gap = d["food"] - d["nonfood"]
    a = d.resample("YE").mean()
    a["gap"] = a["food"] - a["nonfood"]
    print()
    print(a.round(1).to_string())
    print()
    print("years food < non-food      :", int((a["gap"] < 0).sum()), "of", len(a))
    print("widest annual gap          : %.1fpp (%d)" % (a["gap"].min(), a["gap"].idxmin().year))
    print("widest monthly gap         : %.1fpp (%s)" % (
        (-gap).max(), (-gap).idxmax().strftime("%b %Y")))
    print("months food > non-food     : %d of %d" % ((gap > 0).sum(), len(gap)))
    print("  of which in 2020         :", int((gap[gap.index.year == 2020] > 0).sum()))
    print("  largest pre-2020 excess  : %.1fpp (%s)" % (
        gap[gap.index.year < 2020].max(),
        gap[gap.index.year < 2020].idxmax().strftime("%b %Y")))
    print("  largest 2020 excess      : %.1fpp (%s)" % (
        gap[gap.index.year == 2020].max(),
        gap[gap.index.year == 2020].idxmax().strftime("%b %Y")))
    print("series ends                :", d.index[-1].strftime("%b %Y"),
          "— 2020 figures are Jan-Aug only")


if __name__ == "__main__":
    d = load()
    draw(d)
    report(d)
