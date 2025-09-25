'''
Module for creating various data visualizations using Plotly.
Includes functions for line charts, scatter plots, and dumbbell charts.
'''
# import necessary libraries
import plotly.express as px
import plotly.graph_objects as go


def plot_line(df, x, y, x_label=None, y_label=None, legend_label=None, title=None, **kwargs):
    """
    Plot line chart using Plotly.
    Parameters:
    - df: DataFrame containing the data to plot.
    - x: Column name for x-axis.
    - y: List of column names for y-axis.
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

    fig = px.line(df, x=x, y=y, **kwargs)
    fig.update_layout(
        xaxis_title=x_label,
        yaxis_title=y_label,
        legend_title=legend_label,
        title={
            'text': title,
            'x':0.5, # center title
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size':15}
        }
    )
    return fig


def plot_scatter(df, x, y,  x_label=None, y_label=None, legend_label=None, title=None, **kwargs):
    """
    Plot line chart using Plotly.
    Parameters:
    - df: DataFrame containing the data to plot.
    - x: Column name for x-axis.
    - y: List of column names for y-axis.
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

    fig = px.scatter(df, x=x, y=y, **kwargs)
    fig.update_layout(
        xaxis_title=x_label,
        yaxis_title=y_label,
        legend_title=legend_label,
        title={
        'text': title,
        'x':0.5, # center title
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'size':15}
    }
    )
    return fig


def plot_dumbbell(df, x1, x2, y, x_label=None, y_label=None,
                  legend_label=None, title=None, **kwargs):
    """
    Plot line chart using Plotly.
    Parameters:
        - df: DataFrame containing the data to plot.
        - x1: Column name for x-axis for left side of dumbbell.
        - x2: Column name for x-axis for right side of dunbbell.
        - y: column names for y-axis.
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

    # categorical ordering for y-axis
    y_categories = df[y].tolist()

    # Create dumbbell chart
    fig = go.Figure()
    for _, row in df.iterrows():
        # Line connecting Exports and Imports
        fig.add_trace(go.Scatter(
            x=[row[x1], row[x2]],
            y=[row[y], row[y]],
            mode="lines",
            marker=dict(size=10),
            line=dict(color="grey", width=2),
            showlegend=False,
            **kwargs
        ))
    # Add separate markers for Exports and Imports
    # Add markers for Exports
    fig.add_trace(go.Scatter(
        x=df[x1],
        y=df[y],
        mode="markers",
        name=x1,
        marker=dict(color="blue", size=12)
    ))

    # Add markers for Imports
    fig.add_trace(go.Scatter(
        x=df[x2],
        y=df[y],
        mode="markers",
        name=x2,
        marker=dict(color="pink", size=12)
    ))

    # updates labels, title, legend
    fig.update_layout(
        xaxis_title=x_label,
        yaxis_title=y_label,
        legend_title=legend_label,
        title={
        'text': title,
        'x':0.5, # center title
        'xanchor': 'center',
        'yanchor': 'top',
        'font': {'size':15}
        },
        yaxis=dict(
            type='category',
            categoryorder='array',
            categoryarray=y_categories,
            tickmode='array',
            tickvals=y_categories,
            ticktext=y_categories
        )
    )

    return fig
