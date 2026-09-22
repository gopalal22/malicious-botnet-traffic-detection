"""
Common model training and prediction pipeline.

Project:
Malicious Botnet Traffic Detection Using Machine Learning

Member 4:
Evaluation, Results & Ablation
"""


def run_model_pipeline(
    model,
    X_train,
    y_train,
    X_test
):
    """
    Train a model using the supplied training data
    and generate predictions for the test data.

    Parameters
    ----------
    model : object
        A machine learning model implementing fit() and predict().

    X_train : array-like
        Training features.

    y_train : array-like
        Training labels.

    X_test : array-like
        Test features.

    Returns
    -------
    trained_model : object
        The fitted machine learning model.

    y_pred : array-like
        Predictions generated on X_test.
    """

    # ---------------------------------------------------------
    # Input validation
    # ---------------------------------------------------------

    if X_train is None:
        raise ValueError("X_train cannot be None.")

    if y_train is None:
        raise ValueError("y_train cannot be None.")

    if X_test is None:
        raise ValueError("X_test cannot be None.")

    if model is None:
        raise ValueError("Model cannot be None.")

    # ---------------------------------------------------------
    # Train model
    # ---------------------------------------------------------

    model.fit(
        X_train,
        y_train
    )

    # ---------------------------------------------------------
    # Generate predictions
    # ---------------------------------------------------------

    y_pred = model.predict(
        X_test
    )

    return model, y_pred