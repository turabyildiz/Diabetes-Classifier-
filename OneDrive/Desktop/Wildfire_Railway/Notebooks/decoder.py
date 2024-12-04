def decode_file(txt_path, output_csv_path):
    """
    Decodes the raw .txt file into a structured .csv file.

    Parameters:
        txt_path (str): Path to the raw telemetry .txt file.
        output_csv_path (str): Path to save the decoded telemetry .csv file.

    Returns:
        pd.DataFrame: Decoded telemetry data.
    """
    try:
        with open(txt_path, 'r') as file:
            raw_data = file.readlines()

        # Extract telemetry data 
        
        decoded_data = []
        for line in raw_data:
            parts = line.strip().split(',')
            if len(parts) > 5: 
                decoded_data.append({
                    'timestamp': parts[0],
                    'latitude': parts[1],
                    'longitude': parts[2],
                    'altitude': parts[3],
                    'other_field': parts[4]
                })

        df = pd.DataFrame(decoded_data)
        df.to_csv(output_csv_path, index=False)
        print(f"Decoded telemetry saved to {output_csv_path}")
        return df

    except Exception as e:
        print(f"Error decoding file: {e}")
        return None