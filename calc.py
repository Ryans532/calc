

# Input temperature and dewpoint in Fahrenheit
temperature_f = 77  # Temperature in Fahrenheit
dewpoint_f = 68     # Dewpoint in Fahrenheit

# Convert to Celsius
temperature_c = (temperature_f - 32) * 5/9
dewpoint_c = (dewpoint_f - 32) * 5/9

# Calculate saturation vapor pressures for temperature and dewpoint in Celsius
e_temp = 6.11 * math.pow(10, (7.5 * temperature_c) / (temperature_c + 237.3))
e_dew = 6.11 * math.pow(10, (7.5 * dewpoint_c) / (dewpoint_c + 237.3))

# Calculate relative humidity (RH)
relative_humidity = 100 * (e_dew / e_temp)

# Output the result
relative_humidity



# Input temperature and relative humidity in Fahrenheit
temperature_f = 77  # Temperature in Fahrenheit
relative_humidity = 60  # Relative Humidity in %

# Convert temperature to Celsius
temperature_c = (temperature_f - 32) * 5/9

# Calculate saturation vapor pressure for temperature in Celsius
e_temp = 6.11 * math.pow(10, (7.5 * temperature_c) / (temperature_c + 237.3))

# Calculate dewpoint temperature in Celsius
dewpoint_c = (237.3 * math.log(relative_humidity / 100 * e_temp)) / (7.5 * math.log(relative_humidity / 100 * e_temp) - 1)

# Convert dewpoint back to Fahrenheit
dewpoint_f = dewpoint_c * 9/5 + 32

# Output the result
dewpoint_f
