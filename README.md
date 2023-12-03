# Project: API-Custom-Object-Detection

## End-point: https://apple-yolov8-object-detection-jht5j43saa-uc.a.run.app/predict
### Method: POST
>```
>https://apple-yolov8-object-detection-jht5j43saa-uc.a.run.app/predict?image
>```
### Body formdata

|Param|value|Type|
|---|---|---|
|image|Path_to_Image.jpg|file|


### Response

```json
{
    "annotated_image": "decode_latin_image",
    "results": [
        {
            "bounding_box": {
                "x1": 200.62322998046875,
                "x2": 414.0289306640625,
                "y1": 95.6106185913086,
                "y2": 321.9388427734375
            },
            "confidence": 0.9223284721374512,
            "name": "Apple Overripe"
        },
        {
            "bounding_box": {
                "x1": 107.75930786132812,
                "x2": 305.35113525390625,
                "y1": 210.3850555419922,
                "y2": 413.1199951171875
            },
            "confidence": 0.9118185043334961,
            "name": "Apple Overripe"
        },
        {
            "bounding_box": {
                "x1": 120.19114685058594,
                "x2": 312.3899841308594,
                "y1": 9.10952091217041,
                "y2": 209.8932647705078
            },
            "confidence": 0.8971925973892212,
            "name": "Apple Overripe"
        }
    ]
}
```



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
_________________________________________________
Powered By: [postman-to-markdown](https://github.com/bautistaj/postman-to-markdown/)