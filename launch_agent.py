import requests

def get_next_launch():
    data = requests.get("https://api.spacexdata.com/v4/launches/next").json()

    launchpad_id = data["launchpad"]

    pad_data = requests.get(f"https://api.spacexdata.com/v4/launchpads/{launchpad_id}").json()

    return {
        "name":  data["name"],
        "date":  data["date_utc"],
        "city":  pad_data["locality"],      # backup ke liye
        "lat":   pad_data["latitude"],      # new
        "lon":   pad_data["longitude"]      # new
    }
