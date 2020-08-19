# dem_to_occupancy

Converts a
[GridMap](https://github.com/ANYbotics/grid_map/blob/master/grid_map_msgs/msg/GridMap.msg)
to an OccupancyGrid message. This is done via service calls to
`/dem_to_occupancy`.

## How to Use

Prepare a service client of type `dem_to_occupancy/Conversion`. The message
structure is as follows:

```
grid_map_msgs/GridMap grid_map
string layer
float64 threshold
bool retain_unknown
---
nav_msgs/OccupancyGrid grid
```

- `grid_map` is what's going to be converted into OccupancyGrid
- `layer` is the name of the layer to use,
- `threshold` is the threshold to determine whether a grid is occupied or not,
- `retain_unknown` determines whether to leave unknown grids as unknown or
  make them unoccupied.

## License

MIT


## Author

Naoki Mizuno (mizuno.naoki@rm.is.tohoku.ac.jp)
