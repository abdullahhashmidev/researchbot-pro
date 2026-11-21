"""
Chart Engine
------------
Plotly se professional charts banata hai.
"""

from typing import Optional

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pandas.api import types as ptypes


class ChartEngine:

    PRIMARY = "#7b2ff7"
    ACCENT = "#00d2ff"

    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df

    def _numeric_cols(self) -> list:
        """Numeric columns (bool ko chhod kar)"""
        return [
            c for c in self.df.columns
            if ptypes.is_numeric_dtype(self.df[c]) and not ptypes.is_bool_dtype(self.df[c])
        ]

    def correlation_heatmap(self):
        """Numeric columns ka correlation heatmap"""
        numeric_df = self.df[self._numeric_cols()]
        if numeric_df.shape[1] < 2:
            return None

        corr = numeric_df.corr().round(2)
        return px.imshow(
            corr,
            title="Correlation Heatmap",
            color_continuous_scale="RdBu_r",
            zmin=-1,
            zmax=1,
            text_auto=True,
            aspect="auto",
        )

    def missing_values_chart(self):
        """Missing values bar chart"""
        missing = self.df.isnull().sum()
        missing = missing[missing > 0]
        if missing.empty:
            return None

        return px.bar(
            x=missing.index.astype(str),
            y=missing.values,
            title="Missing Values by Column",
            labels={"x": "Column", "y": "Missing Count"},
            color=missing.values,
            color_continuous_scale="Reds",
        )

    def distribution_chart(self, column: str):
        """Column ka distribution (numeric: histogram, baaki: top values)"""
        if column not in self.df.columns:
            return None

        series = self.df[column]
        if ptypes.is_numeric_dtype(series) and not ptypes.is_bool_dtype(series):
            return px.histogram(
                self.df,
                x=column,
                title=f"Distribution: {column}",
                nbins=30,
                color_discrete_sequence=[self.PRIMARY],
            )

        counts = series.value_counts().head(20)
        return px.bar(
            x=counts.index.astype(str),
            y=counts.values,
            title=f"Top Values: {column}",
            labels={"x": column, "y": "Count"},
            color_discrete_sequence=[self.ACCENT],
        )

    def trend_chart(self, x_col: str, y_col: str):
        """Trend line chart (x ke hisaab se sorted)"""
        if x_col not in self.df.columns or y_col not in self.df.columns:
            return None

        data = self.df[[x_col, y_col]].dropna().sort_values(x_col)
        return px.line(
            data,
            x=x_col,
            y=y_col,
            title=f"Trend: {y_col} over {x_col}",
            color_discrete_sequence=[self.ACCENT],
        )

    def kpi_summary_chart(self, numeric_cols: Optional[list] = None):
        """KPI summary table (mean, median, min, max, total).
        Alag scales wale columns ko ek bar chart mein mix karna misleading hota hai,
        isliye table use hoti hai."""
        cols = numeric_cols or self._numeric_cols()
        if not cols:
            return None

        stats = (
            self.df[cols]
            .agg(["mean", "median", "min", "max", "sum"])
            .round(2)
            .T.reset_index()
        )
        stats.columns = ["Metric", "Mean", "Median", "Min", "Max", "Total"]

        return go.Figure(
            data=[go.Table(
                header=dict(values=list(stats.columns), fill_color=self.PRIMARY,
                            font=dict(color="white")),
                cells=dict(values=[stats[c] for c in stats.columns]),
            )],
        )
