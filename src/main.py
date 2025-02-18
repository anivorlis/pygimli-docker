import os
from pygimli.physics import ert


def main() -> None:
    # Read the data [either locally or from the web]
    #data = pg.getExampleData("ert/slagdump.ohm", verbose=True)
    data = ert.load(os.path.join("data", "input", "slagdump.ohm"))

    # Geometric factor
    data['k'] = ert.createGeometricFactors(data, numerical=True)

    # Setup manager
    mgr = ert.ERTManager(sr=False)
    mgr = ert.ERTManager(data)

    data['err'] = ert.estimateError(data, relativeError=0.03, absoluteUError=5e-5)


    model = mgr.invert(data, lam=10, verbose=True,
                    paraDX=0.3, paraMaxCellSize=10, paraDepth=20, quality=33.6)

    ax, cbar = mgr.showResult(model, cMin=5, cMax=30, cMap="Spectral_r", logScale=True)
    ax.figure.savefig(os.path.join("data", "output", "slagdump_model.png"))


if __name__ == "__main__":
    main()
