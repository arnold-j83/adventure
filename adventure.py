from data import locations, locations_extra, objects_in_locations

directions = {
    'west': (-1, 0),
    'east': (1, 0),
    'north': (0, -1),
    'south': (0, 1)
}

position = (0, 0)
objects_picked_up = ""
while True:
    location = locations[position]

    for i in location:
        extra_text = locations_extra[location]
        #items_available = objects_in_locations[location]
    print 'you are at the %s ' % location + " " + extra_text #+ " there are the folling items available: " + objects

    for j in objects_in_locations[location]:
        #objects += j + " "
        print "there are " + j + " to pick up"
    pickup_items = raw_input("which item would you like to pickup? \n")
    if pickup_items:
        objects_picked_up += pickup_items + ", "
        print "items you have picked up: " + objects_picked_up
        valid_directions = {}
        for k, v in directions.iteritems():
            possible_position = (position[0] + v[0], position[1] + v[1])
            possible_location = locations.get(possible_position)
            if possible_location:
                print 'to the %s is a %s' % (k, possible_location)
                valid_directions[k] = possible_position
        direction = raw_input('which direction do you want to go?\n')
        #position = valid_directions[direction]
        new_position = valid_directions.get(direction)
        if new_position:
            position = new_position
        else:
            print "not a valid direction"