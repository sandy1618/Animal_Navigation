;; Auto-generated. Do not edit!


(when (boundp 'dem_to_occupancy::Conversion)
  (if (not (find-package "DEM_TO_OCCUPANCY"))
    (make-package "DEM_TO_OCCUPANCY"))
  (shadow 'Conversion (find-package "DEM_TO_OCCUPANCY")))
(unless (find-package "DEM_TO_OCCUPANCY::CONVERSION")
  (make-package "DEM_TO_OCCUPANCY::CONVERSION"))
(unless (find-package "DEM_TO_OCCUPANCY::CONVERSIONREQUEST")
  (make-package "DEM_TO_OCCUPANCY::CONVERSIONREQUEST"))
(unless (find-package "DEM_TO_OCCUPANCY::CONVERSIONRESPONSE")
  (make-package "DEM_TO_OCCUPANCY::CONVERSIONRESPONSE"))

(in-package "ROS")

(if (not (find-package "GRID_MAP_MSGS"))
  (ros::roseus-add-msgs "grid_map_msgs"))


(if (not (find-package "NAV_MSGS"))
  (ros::roseus-add-msgs "nav_msgs"))


(defclass dem_to_occupancy::ConversionRequest
  :super ros::object
  :slots (_grid_map _layer _threshold _retain_unknown ))

(defmethod dem_to_occupancy::ConversionRequest
  (:init
   (&key
    ((:grid_map __grid_map) (instance grid_map_msgs::GridMap :init))
    ((:layer __layer) "")
    ((:threshold __threshold) 0.0)
    ((:retain_unknown __retain_unknown) nil)
    )
   (send-super :init)
   (setq _grid_map __grid_map)
   (setq _layer (string __layer))
   (setq _threshold (float __threshold))
   (setq _retain_unknown __retain_unknown)
   self)
  (:grid_map
   (&rest __grid_map)
   (if (keywordp (car __grid_map))
       (send* _grid_map __grid_map)
     (progn
       (if __grid_map (setq _grid_map (car __grid_map)))
       _grid_map)))
  (:layer
   (&optional __layer)
   (if __layer (setq _layer __layer)) _layer)
  (:threshold
   (&optional __threshold)
   (if __threshold (setq _threshold __threshold)) _threshold)
  (:retain_unknown
   (&optional __retain_unknown)
   (if __retain_unknown (setq _retain_unknown __retain_unknown)) _retain_unknown)
  (:serialization-length
   ()
   (+
    ;; grid_map_msgs/GridMap _grid_map
    (send _grid_map :serialization-length)
    ;; string _layer
    4 (length _layer)
    ;; float64 _threshold
    8
    ;; bool _retain_unknown
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; grid_map_msgs/GridMap _grid_map
       (send _grid_map :serialize s)
     ;; string _layer
       (write-long (length _layer) s) (princ _layer s)
     ;; float64 _threshold
       (sys::poke _threshold (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; bool _retain_unknown
       (if _retain_unknown (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; grid_map_msgs/GridMap _grid_map
     (send _grid_map :deserialize buf ptr-) (incf ptr- (send _grid_map :serialization-length))
   ;; string _layer
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _layer (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float64 _threshold
     (setq _threshold (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; bool _retain_unknown
     (setq _retain_unknown (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass dem_to_occupancy::ConversionResponse
  :super ros::object
  :slots (_grid ))

(defmethod dem_to_occupancy::ConversionResponse
  (:init
   (&key
    ((:grid __grid) (instance nav_msgs::OccupancyGrid :init))
    )
   (send-super :init)
   (setq _grid __grid)
   self)
  (:grid
   (&rest __grid)
   (if (keywordp (car __grid))
       (send* _grid __grid)
     (progn
       (if __grid (setq _grid (car __grid)))
       _grid)))
  (:serialization-length
   ()
   (+
    ;; nav_msgs/OccupancyGrid _grid
    (send _grid :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; nav_msgs/OccupancyGrid _grid
       (send _grid :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; nav_msgs/OccupancyGrid _grid
     (send _grid :deserialize buf ptr-) (incf ptr- (send _grid :serialization-length))
   ;;
   self)
  )

(defclass dem_to_occupancy::Conversion
  :super ros::object
  :slots ())

(setf (get dem_to_occupancy::Conversion :md5sum-) "8831e923c916b5054320b39c4fd3791a")
(setf (get dem_to_occupancy::Conversion :datatype-) "dem_to_occupancy/Conversion")
(setf (get dem_to_occupancy::Conversion :request) dem_to_occupancy::ConversionRequest)
(setf (get dem_to_occupancy::Conversion :response) dem_to_occupancy::ConversionResponse)

(defmethod dem_to_occupancy::ConversionRequest
  (:response () (instance dem_to_occupancy::ConversionResponse :init)))

(setf (get dem_to_occupancy::ConversionRequest :md5sum-) "8831e923c916b5054320b39c4fd3791a")
(setf (get dem_to_occupancy::ConversionRequest :datatype-) "dem_to_occupancy/ConversionRequest")
(setf (get dem_to_occupancy::ConversionRequest :definition-)
      "
grid_map_msgs/GridMap grid_map

string layer


float64 threshold
bool retain_unknown

================================================================================
MSG: grid_map_msgs/GridMap
# Grid map header
GridMapInfo info

# Grid map layer names.
string[] layers

# Grid map basic layer names (optional). The basic layers
# determine which layers from `layers` need to be valid
# in order for a cell of the grid map to be valid.
string[] basic_layers

# Grid map data.
std_msgs/Float32MultiArray[] data

# Row start index (default 0).
uint16 outer_start_index

# Column start index (default 0).
uint16 inner_start_index

================================================================================
MSG: grid_map_msgs/GridMapInfo
# Header (time and frame)
Header header

# Resolution of the grid [m/cell].
float64 resolution

# Length in x-direction [m].
float64 length_x

# Length in y-direction [m].
float64 length_y

# Pose of the grid map center in the frame defined in `header` [m].
geometry_msgs/Pose pose
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: std_msgs/Float32MultiArray
# Please look at the MultiArrayLayout message definition for
# documentation on all multiarrays.

MultiArrayLayout  layout        # specification of data layout
float32[]         data          # array of data


================================================================================
MSG: std_msgs/MultiArrayLayout
# The multiarray declares a generic multi-dimensional array of a
# particular data type.  Dimensions are ordered from outer most
# to inner most.

MultiArrayDimension[] dim # Array of dimension properties
uint32 data_offset        # padding elements at front of data

# Accessors should ALWAYS be written in terms of dimension stride
# and specified outer-most dimension first.
# 
# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]
#
# A standard, 3-channel 640x480 image with interleaved color channels
# would be specified as:
#
# dim[0].label  = \"height\"
# dim[0].size   = 480
# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)
# dim[1].label  = \"width\"
# dim[1].size   = 640
# dim[1].stride = 3*640 = 1920
# dim[2].label  = \"channel\"
# dim[2].size   = 3
# dim[2].stride = 3
#
# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.

================================================================================
MSG: std_msgs/MultiArrayDimension
string label   # label of given dimension
uint32 size    # size of given dimension (in type units)
---

nav_msgs/OccupancyGrid grid


================================================================================
MSG: nav_msgs/OccupancyGrid
# This represents a 2-D grid map, in which each cell represents the probability of
# occupancy.

Header header 

#MetaData for the map
MapMetaData info

# The map data, in row-major order, starting with (0,0).  Occupancy
# probabilities are in the range [0,100].  Unknown is -1.
int8[] data

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: nav_msgs/MapMetaData
# This hold basic information about the characterists of the OccupancyGrid

# The time at which the map was loaded
time map_load_time
# The map resolution [m/cell]
float32 resolution
# Map width [cells]
uint32 width
# Map height [cells]
uint32 height
# The origin of the map [m, m, rad].  This is the real-world pose of the
# cell (0,0) in the map.
geometry_msgs/Pose origin
================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
")

(setf (get dem_to_occupancy::ConversionResponse :md5sum-) "8831e923c916b5054320b39c4fd3791a")
(setf (get dem_to_occupancy::ConversionResponse :datatype-) "dem_to_occupancy/ConversionResponse")
(setf (get dem_to_occupancy::ConversionResponse :definition-)
      "
grid_map_msgs/GridMap grid_map

string layer


float64 threshold
bool retain_unknown

================================================================================
MSG: grid_map_msgs/GridMap
# Grid map header
GridMapInfo info

# Grid map layer names.
string[] layers

# Grid map basic layer names (optional). The basic layers
# determine which layers from `layers` need to be valid
# in order for a cell of the grid map to be valid.
string[] basic_layers

# Grid map data.
std_msgs/Float32MultiArray[] data

# Row start index (default 0).
uint16 outer_start_index

# Column start index (default 0).
uint16 inner_start_index

================================================================================
MSG: grid_map_msgs/GridMapInfo
# Header (time and frame)
Header header

# Resolution of the grid [m/cell].
float64 resolution

# Length in x-direction [m].
float64 length_x

# Length in y-direction [m].
float64 length_y

# Pose of the grid map center in the frame defined in `header` [m].
geometry_msgs/Pose pose
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: std_msgs/Float32MultiArray
# Please look at the MultiArrayLayout message definition for
# documentation on all multiarrays.

MultiArrayLayout  layout        # specification of data layout
float32[]         data          # array of data


================================================================================
MSG: std_msgs/MultiArrayLayout
# The multiarray declares a generic multi-dimensional array of a
# particular data type.  Dimensions are ordered from outer most
# to inner most.

MultiArrayDimension[] dim # Array of dimension properties
uint32 data_offset        # padding elements at front of data

# Accessors should ALWAYS be written in terms of dimension stride
# and specified outer-most dimension first.
# 
# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]
#
# A standard, 3-channel 640x480 image with interleaved color channels
# would be specified as:
#
# dim[0].label  = \"height\"
# dim[0].size   = 480
# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)
# dim[1].label  = \"width\"
# dim[1].size   = 640
# dim[1].stride = 3*640 = 1920
# dim[2].label  = \"channel\"
# dim[2].size   = 3
# dim[2].stride = 3
#
# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.

================================================================================
MSG: std_msgs/MultiArrayDimension
string label   # label of given dimension
uint32 size    # size of given dimension (in type units)
---

nav_msgs/OccupancyGrid grid


================================================================================
MSG: nav_msgs/OccupancyGrid
# This represents a 2-D grid map, in which each cell represents the probability of
# occupancy.

Header header 

#MetaData for the map
MapMetaData info

# The map data, in row-major order, starting with (0,0).  Occupancy
# probabilities are in the range [0,100].  Unknown is -1.
int8[] data

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: nav_msgs/MapMetaData
# This hold basic information about the characterists of the OccupancyGrid

# The time at which the map was loaded
time map_load_time
# The map resolution [m/cell]
float32 resolution
# Map width [cells]
uint32 width
# Map height [cells]
uint32 height
# The origin of the map [m, m, rad].  This is the real-world pose of the
# cell (0,0) in the map.
geometry_msgs/Pose origin
================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w
")



(provide :dem_to_occupancy/Conversion "8831e923c916b5054320b39c4fd3791a")


