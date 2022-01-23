import preprocessing as pp
import computation as cp
import output

# read the csv files
precipitation = pp.read_csv(path="data/climate_precip.csv")
temperature = pp.read_csv(path="data/climate_temp.csv")

# Extract data points for one station:"GHCND:USW00024215"
precip_one_station = pp.particular_data_point(
    df=precipitation, data_point="GHCND:USW00024215", column_for_the_point="STATION"
)

# Create a new table about one station, including precipitation and temperature data
climate_one_station = pp.inner_join(df1=precip_one_station, df2=temperature)

# Change outliers into NaN
climate_one_station = pp.outliers_to_nan(
    df=climate_one_station,
    column_list=[
        "DLY-PRCP-PCTALL-GE001HI",
        "DLY-SNOW-PCTALL-GE030TI",
        "DLY-HTDD-NORMAL",
    ],
    threshold=0.0,
)

# Fix the datatype of date
climate_one_station = pp.to_datetype(df=climate_one_station, column="DATE")

# Add a month column
climate_one_station = pp.add_month_column(df=climate_one_station, date_column="DATE")

# Create a monthly_climate data
monthly_climate = pp.groupby_sum(
    df=climate_one_station,
    groupby="MONTH",
    extracted_columns=["DLY-PRCP-PCTALL-GE001HI", "DLY-SNOW-PCTALL-GE030TI"],
)

# Compute and add rain_snow_ratio to monthly_climate
rain_snow_ratio = cp.compute_ratio(
    df=monthly_climate,
    numerator="DLY-PRCP-PCTALL-GE001HI",
    denominator="DLY-SNOW-PCTALL-GE030TI",
)

monthly_climate["rain_snow_ratio"] = rain_snow_ratio

# Compute and add Monthly_Heating_Degree to monthly_climate
Monthly_Heating_Degree = pp.groupby_mean(
    df=climate_one_station, groupby="MONTH", extracted_columns=["DLY-HTDD-NORMAL"]
)

monthly_climate["Monthly_Heating_Degree"] = Monthly_Heating_Degree

# Compute and print correlations
correlations = cp.compute_correlations(monthly_climate)
output.print_dict(correlations)

# Make a csv data about monthly climate data
monthly_climate.to_csv("data/output.csv")
