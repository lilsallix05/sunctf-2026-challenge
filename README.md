# The Eternal Flame

| Key | Value |
| --- | --- |
| Challenge Name | The Eternal Flame |
| Author | lilsallix05 |
| Category | OSINT |
| Description | Our operatives intercepted this image from a traveler wandering through a vast desert. We know this fiery pit has been burning for decades, but we need to pinpoint its exact location. Find the coordinates of the center of this crater.<br><br>**Flag Format:** sunctf26{latitude,longitude} in decimal degrees, rounded to exactly 4 decimal places. (Example: `sunctf26{XX.XXXX,XX.XXXX}`)<br><br>**Hint:** The photo was taken in Central Asia. Use Google Maps to explore it :)) |
| Challenge Type | Static |
| Flag | sunctf26{40.2513,58.4371} |
| Score | 100 |

## Solution

<details>
<summary>Click to expand</summary>

1. Analyze the provided image of the burning crater in a desert.
2. Using the hint that the location is in Central Asia, a reverse image search or a keyword search for "burning crater desert Central Asia" reveals the location as the **Darvaza Gas Crater** (also known as the "Gates of Hell") in Turkmenistan.
3. Locate the Darvaza Gas Crater on Google Maps.
4. Extract the exact coordinates of the center of the crater.
5. Format the coordinates to exactly 4 decimal places: Latitude `40.2513`, Longitude `58.4371`.
6. Wrap the coordinates in the required flag format: `sunctf26{40.2513,58.4371}`.

![The Eternal Flame Image](./docs/the_eternal_flame.png)

</details>
