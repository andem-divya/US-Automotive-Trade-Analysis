"""
Module for creating various data visualizations using Plotly.
Includes functions for line charts, scatter plots, dumbbell chart,
grid of line plots, animated sctater plot.
"""
# import necessary libraries
import math

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def plot_line(
    df, x, y, x_label=None, y_label=None, legend_label=None, title=None, **kwargs
):
    """
    Plot line chart using Plotly.
    Parameters:
    - df: DataFrame containing the data to plot.
    - x: Column name for x-axis.
    - y: Column name/names for y-axis. str or list
    - x_label: Label for x-axis.
    - y_label: Label for y-axis.
    - legend_label: Label for the legend.
    - **kwargs: Additional keyword arguments for customization.
    Returns:
    - fig: Plotly figure object.
    Raises:
    - ValueError: If specified columns are not in the DataFrame.
    - TypeError: If input types are incorrect.
    Example:
    plot_line(df, x="Year", y=["Imports", "Exports", "Balance"],
    x_label="Year", y_label="Value", legend_label="Measure", title="Trade Data Over Years")

    """
    # Check that df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError("`df` must be a pandas DataFrame.")

    # Check if x and y columns exist in the DataFrame
    y_cols = [y] if isinstance(y, str) else y
    missing_cols = [col for col in [x, *y_cols] if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing columns in DataFrame: {missing_cols}")

    # plot
    fig = px.line(df, x=x, y=y, **kwargs)
    fig.update_layout(
        xaxis_title=x_label,
        yaxis_title=y_label,
        legend_title=legend_label,
        title={
            "text": title,
            "x": 0.5,  # center title
            "xanchor": "center",
            "yanchor": "top",
            "font": {"size": 15},
        },
    )
    return fig


def plot_scatter(
    df, x, y, x_label=None, y_label=None, legend_label=None, title=None, **kwargs
):
    """
    Plot line chart using Plotly.
    Parameters:
    - df: DataFrame containing the data to plot.
    - x: Column name for x-axis.
    - y: Column name for y-axis.
    - x_label: Label for x-axis.
    - y_label: Label for y-axis.
    - legend_label: Label for the legend.
    - **kwargs: Additional keyword arguments for customization.
    Returns:
    - fig: Plotly figure object.
    Raises:
    - ValueError: If specified columns are not in the DataFrame.
    - TypeError: If input types are incorrect.
    Example:
    plot_scatter(df, x="Year", y="Balance",
    x_label="Year", y_label="Value", title="Trade Data Over Years")

    """
    # Check that df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError("`df` must be a pandas DataFrame.")

    # Check if x and y columns exist in the DataFrame
    y_cols = [y] if isinstance(y, str) else y
    missing_cols = [col for col in [x, *y_cols] if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing columns in DataFrame: {missing_cols}")

    # plot
    fig = px.scatter(df, x=x, y=y, **kwargs)
    fig.update_layout(
        xaxis_title=x_label,
        yaxis_title=y_label,
        legend_title=legend_label,
        title={
            "text": title,
            "x": 0.5,  # center title
            "xanchor": "center",
            "yanchor": "top",
            "font": {"size": 15},
        },
    )

    # Make sure xaxis_title is the same across all facets
    fig.update_xaxes(title_text=x_label)

    return fig


def plot_dumbbell(
    df, x1, x2, y, x_label=None, y_label=None, legend_label=None, title=None, **kwargs
):
    """
    Plot line chart using Plotly.
    Parameters:
        - df: DataFrame containing the data to plot.
        - x1: Column name for x-axis for left side of dumbbell.
        - x2: Column name for x-axis for right side of dunbbell.
        - y: Column name for y-axis.
        - x_label: Label for x-axis.
        - y_label: Label for y-axis.
        - legend_label: Label for the legend.
        - **kwargs: Additional keyword arguments for customization.
    Returns:
        - fig: Plotly figure object.
    Raises:
        - ValueError: If specified columns are not in the DataFrame.
        - TypeError: If input types are incorrect.
    Example:
        plot_dumbbell(
            df=top_countries_df,
            y='Country',
            x1='Export',
            x2='Import',
            x_label="Value (USD)",
            title="Top Trade Partners of the USA: Exports and Imports (2022)",
        )
    """

    # Check that df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError("`df` must be a pandas DataFrame.")

    # Check if x and y columns exist in the DataFrame
    y_cols = [y] if isinstance(y, str) else y
    missing_cols = [col for col in [x1, x2, *y_cols] if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing columns in DataFrame: {missing_cols}")

    # categorical ordering for y-axis
    y_categories = df[y].tolist()

    # Create dumbbell chart
    fig = go.Figure()
    for _, row in df.iterrows():
        # Line connecting Exports and Imports
        fig.add_trace(
            go.Scatter(
                x=[row[x1], row[x2]],
                y=[row[y], row[y]],
                mode="lines",
                marker=dict(size=10),
                line=dict(color="grey", width=2),
                showlegend=False,
                **kwargs,
            )
        )
    # Add separate markers for Exports and Imports
    # Add markers for Exports
    fig.add_trace(
        go.Scatter(
            x=df[x1],
            y=df[y],
            mode="markers",
            name=x1,
            marker=dict(color="blue", size=12),
        )
    )

    # Add markers for Imports
    fig.add_trace(
        go.Scatter(
            x=df[x2],
            y=df[y],
            mode="markers",
            name=x2,
            marker=dict(color="pink", size=12),
        )
    )

    # update grid line
    fig.update_yaxes(
        showgrid=False,  # gridlines for y-axis
    )

    # updates labels, title, legend
    fig.update_layout(
        xaxis_title=x_label,
        yaxis_title=y_label,
        legend_title=legend_label,
        title={
            "text": title,
            "x": 0.5,  # center title
            "xanchor": "center",
            "yanchor": "top",
            "font": {"size": 15},
        },
        yaxis=dict(
            type="category",
            categoryorder="array",
            categoryarray=y_categories,
            tickmode="array",
            tickvals=y_categories,
            ticktext=y_categories,
        ),
    )

    return fig


def plot_bar(
    df,
    x,
    y,
    orientation="h",
    x_label=None,
    y_label=None,
    legend_label=None,
    title=None,
    **kwargs,
):
    """
    Plot bar chart using Plotly.
    Parameters:
    - df: DataFrame containing the data to plot.
    - x: Column name for x-axis.
    - y: Column name for y-axis.
    - orientation: Orientaion of the bars
    - x_label: Label for x-axis.
    - y_label: Label for y-axis.
    - legend_label: Label for the legend.
    - **kwargs: Additional keyword arguments for customization.
    Returns:
    - fig: Plotly figure object.
    Raises:
    - ValueError: If specified columns are not in the DataFrame.
    - TypeError: If input types are incorrect.
    Example:
        px.bar(df, x="total_bill", y="day", orientation='h')
    """

    # Check that df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError("`df` must be a pandas DataFrame.")

    # Validate columns
    if y not in df.columns or x not in df.columns:
        raise ValueError(
            f"DataFrame must contain columns: {x} and {y}.\
                          Available columns: {df.columns.tolist()}"
        )

    # Set figure height so labels don't overlap (approx 30 px per row + padding)
    height = max(400, 30 * len(df) + 120)

    # Create horizontal bar chart
    fig = px.bar(df, x=x, y=y, orientation=orientation, height=height, **kwargs)

    # update layout
    fig.update_layout(
        xaxis_title=x_label,
        yaxis_title=y_label,
        legend_title=legend_label,
        title={
            "text": title,
            "x": 0.5,  # horizontal position of title
            "xanchor": "center",  # how the title text is anchored relative to x
            "yanchor": "top",  # how the title text is anchored relative to x
            "font": {"size": 15},
        },
        yaxis=dict(categoryorder="total ascending"),
        xaxis=dict(showgrid=False),
    )
    return fig


def plot_line_grid(df, x, y1, y2, group_col, groups, n_cols=3, title=None, **kwargs):
    """
    Plot grid of line plots with 2 y axis using Plotly.
    Parameters:
    - df: DataFrame containing the data to plot.
    - x: Column name for x-axis.
    - y1: column names for y-axis.
    - y2: column names for secondary y-axis.
    - group_col: column name to group df on for each subplot
    - groups: list of groups to plot
    - title: title of the plot
    - **kwargs: Additional keyword arguments for customization.
    Returns:
    - fig: Plotly figure object.
    Raises:
    - ValueError: If specified columns are not in the DataFrame.
    - TypeError: If input types are incorrect.
    Example:
        plot_line_grid(top_countries_df, x='Year', y1='Export',
           y2='Tariff on US', group_col='Country', groups=top_countries,
           title = "Export vs Tarrif by Country (Top 10)")
    """
    # Check that df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError("`df` must be a pandas DataFrame.")

    # Check if x, y1, y2 columns exist in the DataFrame
    if y1 not in df.columns or y2 not in df.columns or x not in df.columns:
        raise ValueError(
            f"DataFrame must contain columns: {x},{y1} and {y2}.\
                          Available columns: {df.columns.tolist()}"
        )

    if len(groups) == 0:
        raise ValueError("No {group_col} to plot")

    # grid layout
    n_rows = math.ceil(len(groups) / n_cols)

    # create specs with secondary_y for every subplot
    specs = [[{"secondary_y": True} for _ in range(n_cols)] for _ in range(n_rows)]

    # prepare subplot titles (pad if needed)
    subplot_titles = groups + [""] * (n_rows * n_cols - len(groups))

    fig = make_subplots(
        rows=n_rows,
        cols=n_cols,
        subplot_titles=subplot_titles,
        shared_xaxes=False,
        specs=specs,
    )

    # iterate and add traces per country
    for i, group in enumerate(groups):
        row = i // n_cols + 1
        col = i % n_cols + 1

        group_data = df[df[group_col] == group].sort_values(x)

        # Export value on primary y-axis (hide per-country legend entries)
        fig.add_trace(
            go.Scatter(
                x=group_data[x],
                y=group_data[y1],
                mode="lines+markers",
                # name=f'Y1',
                line=dict(color="blue"),
                showlegend=False,
                **kwargs,
            ),
            row=row,
            col=col,
            secondary_y=False,
        )

        # Tariff rate on secondary y-axis (hide per-country legend entries)
        fig.add_trace(
            go.Scatter(
                x=group_data[x],
                y=group_data[y2],
                mode="lines+markers",
                # name=f'Tariff Rate',
                line=dict(color="red"),
                showlegend=False,
                **kwargs,
            ),
            row=row,
            col=col,
            secondary_y=True,
        )

        # Update y-axis titles for this subplot
        fig.update_yaxes(title_text=y1, row=row, col=col, secondary_y=False)
        fig.update_yaxes(title_text=y2, row=row, col=col, secondary_y=True)

    # Add a single legend mapping colors to metric names (one entry each)
    # We add invisible traces with the desired legend names/colors
    # so the legend shows only these two entries.
    fig.add_trace(
        go.Scatter(x=[None], y=[None], mode="lines", line=dict(color="blue"), name=y1),
        row=1,
        col=1,
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(x=[None], y=[None], mode="lines", line=dict(color="red"), name=y2),
        row=1,
        col=1,
        secondary_y=True,
    )
    # Layout adjustments
    fig.update_layout(
        height=300 * n_rows, width=1200, title_text=title, showlegend=True
    )

    # tighten spacing
    fig.update_layout(margin=dict(t=80, l=50, r=50, b=50))
    return fig


def plot_animated_scatter(df, x_col, y_col, size_col, color_col, title, animation_col):
    """
    Create an animated scatter plot with customizable options.
    Parameters:
    - df (pd.DataFrame): Dataframe containing the data to plot.
    - x_col (str): Column to be used for the x-axis.
    - y_col (str): Column to be used for the y-axis.
    - size_col (str): Column to determine the size of the points.
    - color_col (str): Column to determine the color of the points.
    - title (str): Title of the plot.
    - animation_col (str): Column for the animation frame.
    Returns:
    - fig: Plotly figure object.
    """
    # Use custom_data to pass the animation frame (year) into the hovertemplate
    fig = px.scatter(
        df,
        x=x_col,
        y=y_col,
        size=size_col,
        color=color_col,
        animation_frame=animation_col,
        animation_group=color_col,
        custom_data=[animation_col],
        size_max=60,
        title=title,
        hover_name=color_col,
        template="plotly_white",
    )

    # Define the hovertemplate once
    hover_template = (
        f"<b>%{{hovertext}}</b><br><br>"
        f"{x_col}: $%{{x:,.0f}}<br>"
        f"{y_col}: %{{y:.2f}}%<br>"
        f"{animation_col}: %{{customdata[0]}}<extra></extra>"
    )

    # Apply to base traces
    fig.update_traces(hovertemplate=hover_template)

    # Also apply to each trace inside each animation frame (ensures it's preserved during animation)
    if hasattr(fig, "frames") and fig.frames:
        for frame in fig.frames:
            # frame.data is a tuple/list of traces for that frame
            for trace in frame.data:
                # set hovertemplate for that trace
                trace.hovertemplate = hover_template

    return fig
