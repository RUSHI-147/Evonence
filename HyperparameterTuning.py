#Use GridSearchCV to find the best max_depth (values: [3, 5, 7]) and n_estimators (values: [50, 100]) for a Random Forest classifier.

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
def tune_random_forest(X_train, y_train):
    rf = RandomForestClassifier(random_state=42,n_jobs=-1)
    param_grid = {'max_depth': [3, 5, 7],'n_estimators': [50, 100]}
    grid_search = GridSearchCV(
        estimator=rf,
        param_grid=param_grid,
        cv=5,
        scoring='accuracy',
        n_jobs=-1
    )
    grid_search.fit(X_train, y_train)
    return grid_search
