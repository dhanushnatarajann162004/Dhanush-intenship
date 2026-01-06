{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4c2e63f2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Creating a set (duplicates are automatically removed)\n",
    "s = {1, 2, 3, 4, 1, 2, 7}\n",
    "print(s)  # Output: {1, 2, 3, 4, 7} [00:23:34]\n",
    "\n",
    "# Sets are mutable\n",
    "s.add(50) [00:27:25]\n",
    "s.remove(2) [01:14:01]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d54a6582",
   "metadata": {},
   "outputs": [],
   "source": [
    "fs = frozenset([10, 20, 30, 40]) [00:30:08]\n",
    "# fs.add(50)  # This would throw an error because it is immutable [00:44:30]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "db3fafe7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Basic range (start, stop, step)\n",
    "# Example: numbers from 1 to 9 with a step of 2 [00:55:54]\n",
    "for i in range(1, 10, 2):\n",
    "    print(i) # Output: 1, 3, 5, 7, 9"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7260cc19",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Bytes\n",
    "b = bytes([10, 20, 30])\n",
    "# b[0] = 100 # Error: immutable\n",
    "\n",
    "# Bytearray\n",
    "ba = bytearray([10, 20, 30])\n",
    "ba[0] = 100 # Allowed: mutable [00:47:04]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "54933f7e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Creating a dictionary\n",
    "d = {\"Sanjay\": 20, \"Google\": 40} [01:08:27]\n",
    "\n",
    "# Accessing components\n",
    "print(d.keys())   # Get all keys [01:16:15]\n",
    "print(d.values()) # Get all values [01:16:30]\n",
    "print(d.items())  # Get key-value pairs as tuples [01:16:50]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3c916289",
   "metadata": {},
   "outputs": [],
   "source": [
    "def example_func():\n",
    "    pass\n",
    "\n",
    "result = example_func()\n",
    "print(result) # Output: None"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5948d44c",
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
