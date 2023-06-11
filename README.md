# SONGON_Dash-app

This repository contains a Dash application for visualizing data related to the supraorbital nerve and greater occipital nerve. The application utilizes Plotly library for creating interactive plots.

## Installation

To run this application, you need to have the following dependencies installed:

- `os`
- `pandas` (version 1.3.0 or higher)
- `plotly` (version 4.7.0 or higher)
- `dash` (version 2.0.0 or higher)

You can install the required dependencies using the following command:

```
pip install pandas plotly dash
```

## Usage

1. Clone this repository to your local machine.
2. Make sure you have the required dependencies installed (see Installation section).
3. Open the terminal and navigate to the project directory.
4. Run the following command to start the Dash application:

   ```
   python app.py
   ```

5. Open a web browser and go to `http://127.0.0.1:8050` to access the application.

## Data

The application imports data from a CSV file called `app_data.csv`. Make sure you have this file in the same directory as the `app.py` file. You can modify the data or use a different data source by updating the `df` variable in the code.

## Functionality

The application allows you to select a specimen from a dropdown menu and displays a 3D plot based on the selected specimen. The plot shows the coordinates (x, y, z) of the specimen. You can interact with the plot by zooming, rotating, and panning.
