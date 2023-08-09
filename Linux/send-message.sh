#!/bin/bash
echo "Host:"
read host
echo "Title:"
read title
echo "Message:"
read message
./../dist/toaster -s $host $title $message
