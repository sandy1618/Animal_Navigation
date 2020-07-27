#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/sandy/Animal_Navigation/convert_dem_occupancygrid/src/convert_to_dem"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/sandy/Animal_Navigation/convert_dem_occupancygrid/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/sandy/Animal_Navigation/convert_dem_occupancygrid/install/lib/python2.7/dist-packages:/home/sandy/Animal_Navigation/convert_dem_occupancygrid/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/sandy/Animal_Navigation/convert_dem_occupancygrid/build" \
    "/usr/bin/python2" \
    "/home/sandy/Animal_Navigation/convert_dem_occupancygrid/src/convert_to_dem/setup.py" \
    build --build-base "/home/sandy/Animal_Navigation/convert_dem_occupancygrid/build/convert_to_dem" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/sandy/Animal_Navigation/convert_dem_occupancygrid/install" --install-scripts="/home/sandy/Animal_Navigation/convert_dem_occupancygrid/install/bin"
