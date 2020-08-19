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

echo_and_run cd "/home/kvothe/Animal_Navigation/tohoku_acv_original/src/convert_to_dem"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/kvothe/Animal_Navigation/tohoku_acv_original/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/kvothe/Animal_Navigation/tohoku_acv_original/install/lib/python2.7/dist-packages:/home/kvothe/Animal_Navigation/tohoku_acv_original/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/kvothe/Animal_Navigation/tohoku_acv_original/build" \
    "/usr/bin/python2" \
    "/home/kvothe/Animal_Navigation/tohoku_acv_original/src/convert_to_dem/setup.py" \
    build --build-base "/home/kvothe/Animal_Navigation/tohoku_acv_original/build/convert_to_dem" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/kvothe/Animal_Navigation/tohoku_acv_original/install" --install-scripts="/home/kvothe/Animal_Navigation/tohoku_acv_original/install/bin"
