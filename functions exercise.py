
# If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will 
# still use 4096 bytes of storage. A file made up of 4097 bytes will use 4096*2=8192 bytes of storage. 
# Knowing this, can you fill in the gaps in the calculate_storage function below, which calculates the 
# total number of bytes needed to store a file of a given size?
def calculate_storage(filesize):
    block_size = 4096
    full_blocks = filesize//block_size    # Use floor division to calculate how many blocks are fully occupied  
    partial_block_remainder = filesize%block_size  # Use the modulo operator to check whether there's any remainder
    if partial_block_remainder > 0:
        return block_size*(full_blocks+1)
    return block_size
print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192


# This function converts miles to kilometers (km)
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km
my_trip_miles = 55
my_trip_km = convert_distance(55)
print(f"The distance in kilometers is {my_trip_km}")
print(f"The round-trip in kilometers is {2*my_trip_km}" )


# 2^0=1  2^1=2  2^2=4 , 2 ka power 0 hai 1 so True .....
def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
    while n % 2 == 0:
        num = n / 2
  # If after dividing by two the number is 1, it's a power of two
        if num > 0:
            return True
        return False
    if n == 1:
      return True
    return False
print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False

# Fill in the blanks to make the is_power_of function return whether the number is a power of the given base
def is_power_of(number,base):
  # Base case: when number is smaller than base.
    if number < base:
        if number == 1:
            return base**0 == 1
        else:
            return False
    else:
        nums = number
        while nums!=1 and nums>1:
            nums = nums/base
    # If number is equal to 1, it's a power (base**0).
        if nums<1:
            return False
        return True

  # Recursive case: keep dividing number by base.
print(is_power_of(1,2))
print(is_power_of(2,4))
print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False