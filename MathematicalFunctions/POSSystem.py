{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "unexpected EOF while parsing (<ipython-input-1-59cc859cc5b9>, line 13)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-1-59cc859cc5b9>\"\u001b[0;36m, line \u001b[0;32m13\u001b[0m\n\u001b[0;31m    \u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m unexpected EOF while parsing\n"
     ]
    }
   ],
   "source": [
    "register = 0\n",
    "\n",
    "def GetOrder ():\n",
    "    item = int(input())\n",
    "    if not item:\n",
    "        return ''\n",
    "    quantity = int(input(\"How many?\"))\n",
    "    return item, quantity\n",
    "    \n",
    "while 1:\n",
    "    print(\"Beeronomics Starting Up...\")\n",
    "    print(\"Read to take orders.\")\n",
    "    while 1:\n",
    "        order = []\n",
    "        print(\"What would you like to order? One at a time.\")\n",
    "        print('1. Beer 1\\n'\n",
    "              '2. Beer 2\\n'\n",
    "              '3. Beer 3\\n')\n",
    "        \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    ")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
