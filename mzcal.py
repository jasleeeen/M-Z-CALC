import pyopenms
def calculate_mz(sequence: str, charge: int) -> float:
    peptide = pyopenms.AASequence.fromString(sequence)
    mz = peptide.getMonoWeight() / charge
    return mz