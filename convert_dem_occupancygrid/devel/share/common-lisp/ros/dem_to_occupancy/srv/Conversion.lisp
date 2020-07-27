; Auto-generated. Do not edit!


(cl:in-package dem_to_occupancy-srv)


;//! \htmlinclude Conversion-request.msg.html

(cl:defclass <Conversion-request> (roslisp-msg-protocol:ros-message)
  ((grid_map
    :reader grid_map
    :initarg :grid_map
    :type grid_map_msgs-msg:GridMap
    :initform (cl:make-instance 'grid_map_msgs-msg:GridMap))
   (layer
    :reader layer
    :initarg :layer
    :type cl:string
    :initform "")
   (threshold
    :reader threshold
    :initarg :threshold
    :type cl:float
    :initform 0.0)
   (retain_unknown
    :reader retain_unknown
    :initarg :retain_unknown
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass Conversion-request (<Conversion-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Conversion-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Conversion-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name dem_to_occupancy-srv:<Conversion-request> is deprecated: use dem_to_occupancy-srv:Conversion-request instead.")))

(cl:ensure-generic-function 'grid_map-val :lambda-list '(m))
(cl:defmethod grid_map-val ((m <Conversion-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dem_to_occupancy-srv:grid_map-val is deprecated.  Use dem_to_occupancy-srv:grid_map instead.")
  (grid_map m))

(cl:ensure-generic-function 'layer-val :lambda-list '(m))
(cl:defmethod layer-val ((m <Conversion-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dem_to_occupancy-srv:layer-val is deprecated.  Use dem_to_occupancy-srv:layer instead.")
  (layer m))

(cl:ensure-generic-function 'threshold-val :lambda-list '(m))
(cl:defmethod threshold-val ((m <Conversion-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dem_to_occupancy-srv:threshold-val is deprecated.  Use dem_to_occupancy-srv:threshold instead.")
  (threshold m))

(cl:ensure-generic-function 'retain_unknown-val :lambda-list '(m))
(cl:defmethod retain_unknown-val ((m <Conversion-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dem_to_occupancy-srv:retain_unknown-val is deprecated.  Use dem_to_occupancy-srv:retain_unknown instead.")
  (retain_unknown m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Conversion-request>) ostream)
  "Serializes a message object of type '<Conversion-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'grid_map) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'layer))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'layer))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'threshold))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'retain_unknown) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Conversion-request>) istream)
  "Deserializes a message object of type '<Conversion-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'grid_map) istream)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'layer) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'layer) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'threshold) (roslisp-utils:decode-double-float-bits bits)))
    (cl:setf (cl:slot-value msg 'retain_unknown) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Conversion-request>)))
  "Returns string type for a service object of type '<Conversion-request>"
  "dem_to_occupancy/ConversionRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Conversion-request)))
  "Returns string type for a service object of type 'Conversion-request"
  "dem_to_occupancy/ConversionRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Conversion-request>)))
  "Returns md5sum for a message object of type '<Conversion-request>"
  "8831e923c916b5054320b39c4fd3791a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Conversion-request)))
  "Returns md5sum for a message object of type 'Conversion-request"
  "8831e923c916b5054320b39c4fd3791a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Conversion-request>)))
  "Returns full string definition for message of type '<Conversion-request>"
  (cl:format cl:nil "~%grid_map_msgs/GridMap grid_map~%~%string layer~%~%~%float64 threshold~%bool retain_unknown~%~%================================================================================~%MSG: grid_map_msgs/GridMap~%# Grid map header~%GridMapInfo info~%~%# Grid map layer names.~%string[] layers~%~%# Grid map basic layer names (optional). The basic layers~%# determine which layers from `layers` need to be valid~%# in order for a cell of the grid map to be valid.~%string[] basic_layers~%~%# Grid map data.~%std_msgs/Float32MultiArray[] data~%~%# Row start index (default 0).~%uint16 outer_start_index~%~%# Column start index (default 0).~%uint16 inner_start_index~%~%================================================================================~%MSG: grid_map_msgs/GridMapInfo~%# Header (time and frame)~%Header header~%~%# Resolution of the grid [m/cell].~%float64 resolution~%~%# Length in x-direction [m].~%float64 length_x~%~%# Length in y-direction [m].~%float64 length_y~%~%# Pose of the grid map center in the frame defined in `header` [m].~%geometry_msgs/Pose pose~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: std_msgs/Float32MultiArray~%# Please look at the MultiArrayLayout message definition for~%# documentation on all multiarrays.~%~%MultiArrayLayout  layout        # specification of data layout~%float32[]         data          # array of data~%~%~%================================================================================~%MSG: std_msgs/MultiArrayLayout~%# The multiarray declares a generic multi-dimensional array of a~%# particular data type.  Dimensions are ordered from outer most~%# to inner most.~%~%MultiArrayDimension[] dim # Array of dimension properties~%uint32 data_offset        # padding elements at front of data~%~%# Accessors should ALWAYS be written in terms of dimension stride~%# and specified outer-most dimension first.~%# ~%# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]~%#~%# A standard, 3-channel 640x480 image with interleaved color channels~%# would be specified as:~%#~%# dim[0].label  = \"height\"~%# dim[0].size   = 480~%# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)~%# dim[1].label  = \"width\"~%# dim[1].size   = 640~%# dim[1].stride = 3*640 = 1920~%# dim[2].label  = \"channel\"~%# dim[2].size   = 3~%# dim[2].stride = 3~%#~%# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.~%~%================================================================================~%MSG: std_msgs/MultiArrayDimension~%string label   # label of given dimension~%uint32 size    # size of given dimension (in type units)~%uint32 stride  # stride of given dimension~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Conversion-request)))
  "Returns full string definition for message of type 'Conversion-request"
  (cl:format cl:nil "~%grid_map_msgs/GridMap grid_map~%~%string layer~%~%~%float64 threshold~%bool retain_unknown~%~%================================================================================~%MSG: grid_map_msgs/GridMap~%# Grid map header~%GridMapInfo info~%~%# Grid map layer names.~%string[] layers~%~%# Grid map basic layer names (optional). The basic layers~%# determine which layers from `layers` need to be valid~%# in order for a cell of the grid map to be valid.~%string[] basic_layers~%~%# Grid map data.~%std_msgs/Float32MultiArray[] data~%~%# Row start index (default 0).~%uint16 outer_start_index~%~%# Column start index (default 0).~%uint16 inner_start_index~%~%================================================================================~%MSG: grid_map_msgs/GridMapInfo~%# Header (time and frame)~%Header header~%~%# Resolution of the grid [m/cell].~%float64 resolution~%~%# Length in x-direction [m].~%float64 length_x~%~%# Length in y-direction [m].~%float64 length_y~%~%# Pose of the grid map center in the frame defined in `header` [m].~%geometry_msgs/Pose pose~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: std_msgs/Float32MultiArray~%# Please look at the MultiArrayLayout message definition for~%# documentation on all multiarrays.~%~%MultiArrayLayout  layout        # specification of data layout~%float32[]         data          # array of data~%~%~%================================================================================~%MSG: std_msgs/MultiArrayLayout~%# The multiarray declares a generic multi-dimensional array of a~%# particular data type.  Dimensions are ordered from outer most~%# to inner most.~%~%MultiArrayDimension[] dim # Array of dimension properties~%uint32 data_offset        # padding elements at front of data~%~%# Accessors should ALWAYS be written in terms of dimension stride~%# and specified outer-most dimension first.~%# ~%# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]~%#~%# A standard, 3-channel 640x480 image with interleaved color channels~%# would be specified as:~%#~%# dim[0].label  = \"height\"~%# dim[0].size   = 480~%# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)~%# dim[1].label  = \"width\"~%# dim[1].size   = 640~%# dim[1].stride = 3*640 = 1920~%# dim[2].label  = \"channel\"~%# dim[2].size   = 3~%# dim[2].stride = 3~%#~%# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.~%~%================================================================================~%MSG: std_msgs/MultiArrayDimension~%string label   # label of given dimension~%uint32 size    # size of given dimension (in type units)~%uint32 stride  # stride of given dimension~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Conversion-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'grid_map))
     4 (cl:length (cl:slot-value msg 'layer))
     8
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Conversion-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Conversion-request
    (cl:cons ':grid_map (grid_map msg))
    (cl:cons ':layer (layer msg))
    (cl:cons ':threshold (threshold msg))
    (cl:cons ':retain_unknown (retain_unknown msg))
))
;//! \htmlinclude Conversion-response.msg.html

(cl:defclass <Conversion-response> (roslisp-msg-protocol:ros-message)
  ((grid
    :reader grid
    :initarg :grid
    :type nav_msgs-msg:OccupancyGrid
    :initform (cl:make-instance 'nav_msgs-msg:OccupancyGrid)))
)

(cl:defclass Conversion-response (<Conversion-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Conversion-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Conversion-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name dem_to_occupancy-srv:<Conversion-response> is deprecated: use dem_to_occupancy-srv:Conversion-response instead.")))

(cl:ensure-generic-function 'grid-val :lambda-list '(m))
(cl:defmethod grid-val ((m <Conversion-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader dem_to_occupancy-srv:grid-val is deprecated.  Use dem_to_occupancy-srv:grid instead.")
  (grid m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Conversion-response>) ostream)
  "Serializes a message object of type '<Conversion-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'grid) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Conversion-response>) istream)
  "Deserializes a message object of type '<Conversion-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'grid) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Conversion-response>)))
  "Returns string type for a service object of type '<Conversion-response>"
  "dem_to_occupancy/ConversionResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Conversion-response)))
  "Returns string type for a service object of type 'Conversion-response"
  "dem_to_occupancy/ConversionResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Conversion-response>)))
  "Returns md5sum for a message object of type '<Conversion-response>"
  "8831e923c916b5054320b39c4fd3791a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Conversion-response)))
  "Returns md5sum for a message object of type 'Conversion-response"
  "8831e923c916b5054320b39c4fd3791a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Conversion-response>)))
  "Returns full string definition for message of type '<Conversion-response>"
  (cl:format cl:nil "~%nav_msgs/OccupancyGrid grid~%~%~%================================================================================~%MSG: nav_msgs/OccupancyGrid~%# This represents a 2-D grid map, in which each cell represents the probability of~%# occupancy.~%~%Header header ~%~%#MetaData for the map~%MapMetaData info~%~%# The map data, in row-major order, starting with (0,0).  Occupancy~%# probabilities are in the range [0,100].  Unknown is -1.~%int8[] data~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: nav_msgs/MapMetaData~%# This hold basic information about the characterists of the OccupancyGrid~%~%# The time at which the map was loaded~%time map_load_time~%# The map resolution [m/cell]~%float32 resolution~%# Map width [cells]~%uint32 width~%# Map height [cells]~%uint32 height~%# The origin of the map [m, m, rad].  This is the real-world pose of the~%# cell (0,0) in the map.~%geometry_msgs/Pose origin~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Conversion-response)))
  "Returns full string definition for message of type 'Conversion-response"
  (cl:format cl:nil "~%nav_msgs/OccupancyGrid grid~%~%~%================================================================================~%MSG: nav_msgs/OccupancyGrid~%# This represents a 2-D grid map, in which each cell represents the probability of~%# occupancy.~%~%Header header ~%~%#MetaData for the map~%MapMetaData info~%~%# The map data, in row-major order, starting with (0,0).  Occupancy~%# probabilities are in the range [0,100].  Unknown is -1.~%int8[] data~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: nav_msgs/MapMetaData~%# This hold basic information about the characterists of the OccupancyGrid~%~%# The time at which the map was loaded~%time map_load_time~%# The map resolution [m/cell]~%float32 resolution~%# Map width [cells]~%uint32 width~%# Map height [cells]~%uint32 height~%# The origin of the map [m, m, rad].  This is the real-world pose of the~%# cell (0,0) in the map.~%geometry_msgs/Pose origin~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Conversion-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'grid))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Conversion-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Conversion-response
    (cl:cons ':grid (grid msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Conversion)))
  'Conversion-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Conversion)))
  'Conversion-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Conversion)))
  "Returns string type for a service object of type '<Conversion>"
  "dem_to_occupancy/Conversion")