{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f2bf606b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "After append: [1, 2, 'Python', 3.14, True, 100]\n",
      "After insert at index 0: ['Start', 1, 2, 'Python', 3.14, True, 100]\n",
      "After remove 'Python': ['Start', 1, 2, 3.14, True, 100]\n",
      "Popped value: 100\n"
     ]
    }
   ],
   "source": [
    "# Creating a list with multiple data types\n",
    "my_list = [1, 2, \"Python\", 3.14, True]\n",
    "\n",
    "# Appending an element to the end \n",
    "my_list.append(100)\n",
    "print(\"After append:\", my_list)\n",
    "\n",
    "# Inserting an element at a specific index # Syntax: insert(index, object)\n",
    "my_list.insert(0, \"Start\") \n",
    "print(\"After insert at index 0:\", my_list)\n",
    "\n",
    "# Removing an element by value \n",
    "# Removes the first occurrence of the value\n",
    "my_list.remove(\"Python\")\n",
    "print(\"After remove 'Python':\", my_list)\n",
    "\n",
    "# Popping (deleting and returning) an element \n",
    "# By default, it pops the last element (index -1)\n",
    "last_val = my_list.pop()\n",
    "print(\"Popped value:\", last_val)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9cd3b762",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "60\n",
      "[20, 30, 40]\n",
      "[60, 50, 40, 30, 20, 10]\n"
     ]
    }
   ],
   "source": [
    "numbers = [10, 20, 30, 40, 50, 60]\n",
    "\n",
    "# Positive indexing starts from 0\n",
    "print(numbers[0])  # 10\n",
    "\n",
    "# Negative indexing starts from -1 from the right \n",
    "print(numbers[-1]) # 60\n",
    "\n",
    "# Slicing [start:stop:step] \n",
    "print(numbers[1:4])   # Output: [20, 30, 40]\n",
    "print(numbers[::-1])  # Reverses the list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b9043547",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Lists are mutable\n",
    "l = [1, 2, 3]\n",
    "l[0] = 10  # This is allowed\n",
    "\n",
    "# Tuples are immutable\n",
    "t = (1, 2, 3)\n",
    "# t[0] = 10 # This would throw a TypeError "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "187f56a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Count of 2: 3\n",
      "Index of 4: 4\n"
     ]
    }
   ],
   "source": [
    "my_tuple = (1, 2, 3, 2, 4, 2)\n",
    "\n",
    "# Count occurrences of a value\n",
    "print(\"Count of 2:\", my_tuple.count(2)) # Output: 3\n",
    "\n",
    "# Find the index of a value \n",
    "print(\"Index of 4:\", my_tuple.index(4)) # Output: 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "41883596",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sorted: [12, 33, 45, 89]\n",
      "Descending: [89, 45, 33, 12]\n",
      "Extended list: [1, 2, 3, 4]\n"
     ]
    }
   ],
   "source": [
    "# Sorting a list \n",
    "data = [45, 12, 89, 33]\n",
    "data.sort() # Ascending order by default \n",
    "print(\"Sorted:\", data)\n",
    "\n",
    "# Sorting in descending order \n",
    "data.sort(reverse=True)\n",
    "print(\"Descending:\", data)\n",
    "\n",
    "\n",
    "list_a = [1, 2]\n",
    "list_b = [3, 4]\n",
    "list_a.extend(list_b)\n",
    "print(\"Extended list:\", list_a) # Output: [1, 2, 3, 4]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "af250c78",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
