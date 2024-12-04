def interpolate_telemetry(telemetry_data, frame_timestamps):
    """
    Interpolates telemetry data to align with video frame timestamps.

    Parameters:
        telemetry_data (pd.DataFrame): Telemetry data with 'timestamp' and other fields.
        frame_timestamps (list or np.array): List of frame timestamps (in milliseconds).

    Returns:
        pd.DataFrame: Interpolated telemetry data aligned with frame timestamps.
    """
    telemetry_data['timestamp'] = pd.to_datetime(telemetry_data['timestamp'])
    telemetry_data['timestamp_ms'] = telemetry_data['timestamp'].astype(np.int64) // 10**6

    interpolated = pd.DataFrame({'frame_timestamp': frame_timestamps})
    for col in telemetry_data.columns:
        if col not in ['timestamp', 'timestamp_ms']:
            interpolated[col] = np.interp(
                frame_timestamps,
                telemetry_data['timestamp_ms'],
                telemetry_data[col]
            )

    return interpolated