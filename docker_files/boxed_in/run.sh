#!/bin/sh
socat tcp-l:5000,fork,reuseaddr exec:./boxed_in