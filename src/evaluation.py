import numpy as np
import pandas as pd

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


def evaluate_models(trained_models, x_test, y_test):

    results = []

    for name, model in trained_models.items():

        # Prediction
        y_pred = model.predict(x_test)

        # Metrics
        mae = mean_absolute_error(y_test, y_pred)

        rmse = np.sqrt(
            mean_squared_error(y_test, y_pred)
        )

        r2 = r2_score(y_test, y_pred)

        # Store results
        results.append({
            "Model": name,
            "MAE": mae,
            "RMSE": rmse,
            "R2 Score": r2
        })

    # Convert results to DataFrame
    results = pd.DataFrame(results)

    # Sort by R2 score
    results = results.sort_values(
        by="R2 Score",
        ascending=False
    )

    return results
