// Auto-generated. Do not edit!

// (in-package dem_to_occupancy.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let grid_map_msgs = _finder('grid_map_msgs');

//-----------------------------------------------------------

let nav_msgs = _finder('nav_msgs');

//-----------------------------------------------------------

class ConversionRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.grid_map = null;
      this.layer = null;
      this.threshold = null;
      this.retain_unknown = null;
    }
    else {
      if (initObj.hasOwnProperty('grid_map')) {
        this.grid_map = initObj.grid_map
      }
      else {
        this.grid_map = new grid_map_msgs.msg.GridMap();
      }
      if (initObj.hasOwnProperty('layer')) {
        this.layer = initObj.layer
      }
      else {
        this.layer = '';
      }
      if (initObj.hasOwnProperty('threshold')) {
        this.threshold = initObj.threshold
      }
      else {
        this.threshold = 0.0;
      }
      if (initObj.hasOwnProperty('retain_unknown')) {
        this.retain_unknown = initObj.retain_unknown
      }
      else {
        this.retain_unknown = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ConversionRequest
    // Serialize message field [grid_map]
    bufferOffset = grid_map_msgs.msg.GridMap.serialize(obj.grid_map, buffer, bufferOffset);
    // Serialize message field [layer]
    bufferOffset = _serializer.string(obj.layer, buffer, bufferOffset);
    // Serialize message field [threshold]
    bufferOffset = _serializer.float64(obj.threshold, buffer, bufferOffset);
    // Serialize message field [retain_unknown]
    bufferOffset = _serializer.bool(obj.retain_unknown, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ConversionRequest
    let len;
    let data = new ConversionRequest(null);
    // Deserialize message field [grid_map]
    data.grid_map = grid_map_msgs.msg.GridMap.deserialize(buffer, bufferOffset);
    // Deserialize message field [layer]
    data.layer = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [threshold]
    data.threshold = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [retain_unknown]
    data.retain_unknown = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += grid_map_msgs.msg.GridMap.getMessageSize(object.grid_map);
    length += object.layer.length;
    return length + 13;
  }

  static datatype() {
    // Returns string type for a service object
    return 'dem_to_occupancy/ConversionRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'b2f947c0d469b93b56bbb8e0fab7f286';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
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
    # dim[0].label  = "height"
    # dim[0].size   = 480
    # dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)
    # dim[1].label  = "width"
    # dim[1].size   = 640
    # dim[1].stride = 3*640 = 1920
    # dim[2].label  = "channel"
    # dim[2].size   = 3
    # dim[2].stride = 3
    #
    # multiarray(i,j,k) refers to the ith row, jth column, and kth channel.
    
    ================================================================================
    MSG: std_msgs/MultiArrayDimension
    string label   # label of given dimension
    uint32 size    # size of given dimension (in type units)
    uint32 stride  # stride of given dimension
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ConversionRequest(null);
    if (msg.grid_map !== undefined) {
      resolved.grid_map = grid_map_msgs.msg.GridMap.Resolve(msg.grid_map)
    }
    else {
      resolved.grid_map = new grid_map_msgs.msg.GridMap()
    }

    if (msg.layer !== undefined) {
      resolved.layer = msg.layer;
    }
    else {
      resolved.layer = ''
    }

    if (msg.threshold !== undefined) {
      resolved.threshold = msg.threshold;
    }
    else {
      resolved.threshold = 0.0
    }

    if (msg.retain_unknown !== undefined) {
      resolved.retain_unknown = msg.retain_unknown;
    }
    else {
      resolved.retain_unknown = false
    }

    return resolved;
    }
};

class ConversionResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.grid = null;
    }
    else {
      if (initObj.hasOwnProperty('grid')) {
        this.grid = initObj.grid
      }
      else {
        this.grid = new nav_msgs.msg.OccupancyGrid();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ConversionResponse
    // Serialize message field [grid]
    bufferOffset = nav_msgs.msg.OccupancyGrid.serialize(obj.grid, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ConversionResponse
    let len;
    let data = new ConversionResponse(null);
    // Deserialize message field [grid]
    data.grid = nav_msgs.msg.OccupancyGrid.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += nav_msgs.msg.OccupancyGrid.getMessageSize(object.grid);
    return length;
  }

  static datatype() {
    // Returns string type for a service object
    return 'dem_to_occupancy/ConversionResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '794bee16056dd99c4e79450f52ea1470';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ConversionResponse(null);
    if (msg.grid !== undefined) {
      resolved.grid = nav_msgs.msg.OccupancyGrid.Resolve(msg.grid)
    }
    else {
      resolved.grid = new nav_msgs.msg.OccupancyGrid()
    }

    return resolved;
    }
};

module.exports = {
  Request: ConversionRequest,
  Response: ConversionResponse,
  md5sum() { return '8831e923c916b5054320b39c4fd3791a'; },
  datatype() { return 'dem_to_occupancy/Conversion'; }
};
