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

echo_and_run cd "/home/kvothe/Animal_Navigation/navigation/src/base_local_planner"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/kvothe/Animal_Navigation/navigation/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/kvothe/Animal_Navigation/navigation/install/lib/python2.7/dist-packages:/home/kvothe/Animal_Navigation/navigation/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/kvothe/Animal_Navigation/navigation/build" \
    "/usr/bin/python2" \
    "/home/kvothe/Animal_Navigation/navigation/src/base_local_planner/setup.py" \
    build --build-base "/home/kvothe/Animal_Navigation/navigation/build/base_local_planner" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/kvothe/Animal_Navigation/navigation/install" --install-scripts="/home/kvothe/Animal_Navigation/navigation/install/bin"
