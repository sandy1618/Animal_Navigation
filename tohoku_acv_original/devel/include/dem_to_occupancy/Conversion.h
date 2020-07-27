// Generated by gencpp from file dem_to_occupancy/Conversion.msg
// DO NOT EDIT!


#ifndef DEM_TO_OCCUPANCY_MESSAGE_CONVERSION_H
#define DEM_TO_OCCUPANCY_MESSAGE_CONVERSION_H

#include <ros/service_traits.h>


#include <dem_to_occupancy/ConversionRequest.h>
#include <dem_to_occupancy/ConversionResponse.h>


namespace dem_to_occupancy
{

struct Conversion
{

typedef ConversionRequest Request;
typedef ConversionResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct Conversion
} // namespace dem_to_occupancy


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::dem_to_occupancy::Conversion > {
  static const char* value()
  {
    return "8831e923c916b5054320b39c4fd3791a";
  }

  static const char* value(const ::dem_to_occupancy::Conversion&) { return value(); }
};

template<>
struct DataType< ::dem_to_occupancy::Conversion > {
  static const char* value()
  {
    return "dem_to_occupancy/Conversion";
  }

  static const char* value(const ::dem_to_occupancy::Conversion&) { return value(); }
};


// service_traits::MD5Sum< ::dem_to_occupancy::ConversionRequest> should match 
// service_traits::MD5Sum< ::dem_to_occupancy::Conversion > 
template<>
struct MD5Sum< ::dem_to_occupancy::ConversionRequest>
{
  static const char* value()
  {
    return MD5Sum< ::dem_to_occupancy::Conversion >::value();
  }
  static const char* value(const ::dem_to_occupancy::ConversionRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::dem_to_occupancy::ConversionRequest> should match 
// service_traits::DataType< ::dem_to_occupancy::Conversion > 
template<>
struct DataType< ::dem_to_occupancy::ConversionRequest>
{
  static const char* value()
  {
    return DataType< ::dem_to_occupancy::Conversion >::value();
  }
  static const char* value(const ::dem_to_occupancy::ConversionRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::dem_to_occupancy::ConversionResponse> should match 
// service_traits::MD5Sum< ::dem_to_occupancy::Conversion > 
template<>
struct MD5Sum< ::dem_to_occupancy::ConversionResponse>
{
  static const char* value()
  {
    return MD5Sum< ::dem_to_occupancy::Conversion >::value();
  }
  static const char* value(const ::dem_to_occupancy::ConversionResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::dem_to_occupancy::ConversionResponse> should match 
// service_traits::DataType< ::dem_to_occupancy::Conversion > 
template<>
struct DataType< ::dem_to_occupancy::ConversionResponse>
{
  static const char* value()
  {
    return DataType< ::dem_to_occupancy::Conversion >::value();
  }
  static const char* value(const ::dem_to_occupancy::ConversionResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // DEM_TO_OCCUPANCY_MESSAGE_CONVERSION_H
