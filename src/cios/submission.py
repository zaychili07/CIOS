import pandas as pd


SUBMISSION_COLUMNS = [
    "id",
    "dataset",
    "row_type",
    "node_id",
    "t",
    "z",
    "y",
    "x",
    "source_id",
    "target_id",
]


def build_submission(nodes: pd.DataFrame, edges: pd.DataFrame) -> pd.DataFrame:
    """
    Build Kaggle submission with node and edge rows.
    """

    submission = pd.concat([nodes, edges], ignore_index=True)
    submission = submission[SUBMISSION_COLUMNS]
    submission["id"] = range(len(submission))

    return submission