#% operator %s for string %d for integer %f for loat
print("currently we are having %s class" %"PRG101")
subject = 'Python'
module_no = 2.9999999
print("the moduel number of %s is %.2f" %(subject, module_no))# space% to identify the %d,%sand%f
#format method
print("we are in unit {}".format(2))
print("{p} is a programming langauge. with the help of {p} we can create various" \
" applications. {p} is an {i} langauge".format(p='Python',i='interpreted') )#.format to identify {}
# f string
topic = "formatting string"
print(f"we are currently learning {topic}")
print(f"There are 12 girls and 16 boys in our class.soin total we have {12+16} students")