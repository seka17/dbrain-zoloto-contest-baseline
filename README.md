## Description

Baseline solution for [zoloto contest](https://ds.dbrain.io/contests/7ceabfe1-ae62-46dc-b8a1-507b5d1875db)

Labels are presented in `markup.json`, each key is path to file inside folder, and value is markup as follows:
  * `aabb` is dictionary containing keys, which can be omitted for this contest. Each key points to array of polygons. Format of polygons is geoJSON, which means that each polygon described with 5 points [x, y], where last point equals to the first one.
  * `image_label` is a string contining value of target to predict.

Your solution need to returns values as they're presented in markup, but you can omit `aabb` part.
Example:
```
{
  "image_label": "ф1-о898"
}
```

## Developing

It's required to preserve naming, there must be a file named `ds_model.py` and it must have `DSModel` class, implementing all required methods described on contests page.

For testing purpose you can write main part of `ds_model.py` file, see it for example.

## Submitting

In order to submit you need to provide code archive, publicly accessible docker image and assets if required.
To submit this baseline do as follows:
  1. Archive code `tar -czf ds_model.tar.gz ds_model.py`
  2. Choose image fitting your environment (`dbrain/base:latest` for this example)
  3. Profit!
