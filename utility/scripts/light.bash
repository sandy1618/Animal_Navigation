#!/bin/bash
sudo su
roslaunch spatial_driver output_anpp_complete.launch&
sleep 10
roslaunch move_animal move_animal_led_sig.launch