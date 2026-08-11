from sklearn.pipeline import Pipeline

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor


def train_models(pre, x_train, y_train):

    models = {
        "Linear Regression": LinearRegression(),

        "Decision Tree": DecisionTreeRegressor(
            random_state=42
        ),

        "Random Forest": RandomForestRegressor(
            random_state=42
        ),

        "XGBoost": XGBRegressor(
            random_state=42
        )
    }

    trained_models = {}

    for name, model in models.items():

        pipeline = Pipeline([
            ("preprocessor", pre),
            ("model", model)
        ])

        pipeline.fit(x_train, y_train)

        trained_models[name] = pipeline

    return trained_models