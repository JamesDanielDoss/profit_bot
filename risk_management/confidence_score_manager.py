import pandas as pd

def calculate_confidence_score(data):
    """
    Calculates confidence scores based on signal strength. 
    A higher score indicates a stronger signal (e.g., a wider gap between short and long moving averages).
    """
    data['Confidence'] = abs(data['SMA_short'] - data['SMA_long']) / data['SMA_long']
    data['Confidence'] = data['Confidence'].fillna(0)  # Replace NaNs with 0 for initial rows
    
    # Scale confidence scores between 0 and 1
    data['Confidence'] = data['Confidence'].clip(0, 1)
    
    return data

if __name__ == "__main__":
    # Test with sample data
    test_data = pd.DataFrame({
        'Close': [3200, 3220, 3215, 3230, 3245, 3250, 3260, 3280, 3270, 3300],
        'SMA_short': [3200, 3210, 3212, 3220, 3235, 3245, 3260, 3275, 3280, 3290],
        'SMA_long': [3200, 3210, 3215, 3218, 3230, 3240, 3250, 3265, 3275, 3285],
        'Signal': [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
    })

    # Calculate confidence scores
    data_with_confidence = calculate_confidence_score(test_data)
    print(data_with_confidence[['Close', 'SMA_short', 'SMA_long', 'Signal', 'Confidence']])
