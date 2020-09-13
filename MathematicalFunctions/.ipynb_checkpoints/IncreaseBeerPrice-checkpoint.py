{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the Beer ID 1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5.81\n",
      "The Update was successful.\n"
     ]
    }
   ],
   "source": [
    "import mysql.connector\n",
    "import time\n",
    "\n",
    "Id = int(input(\"Enter the Beer ID\"))\n",
    "\n",
    "if Id > 0:\n",
    "    connection = mysql.connector.connect(host='localhost', # Setting up the database connection\n",
    "                                         database = 'beeronomics',\n",
    "                                         user='root',\n",
    "                                         password='Cheers!!')\n",
    "    cursor1 = connection.cursor(buffered = True)\n",
    "    cursor2 = connection.cursor(buffered = True)\n",
    "    \n",
    "    mySql_Select_Beer_Price = \"\"\"SELECT beer_price_active FROM beer_types WHERE beer_id = %s\"\"\"\n",
    "    mySql_Update_Beer_Price = \"\"\"UPDATE beer_types SET beer_price_active = %s WHERE beer_id = %s\"\"\"\n",
    "    result = cursor1.execute(mySql_Select_Beer_Price,(Id,))\n",
    "    record = cursor1.fetchone()\n",
    "    old_beer_price = record[0]\n",
    "    \n",
    "    new_beer_price = old_beer_price + 0.50\n",
    "    \n",
    "    print(new_beer_price)\n",
    "    \n",
    "    update = cursor2.execute(mySql_Update_Beer_Price,(new_beer_price,Id,))\n",
    "    action = connection.commit()\n",
    "    \n",
    "    print(\"The Update was successful.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
