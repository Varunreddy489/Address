DB_HOST="localhost"
DB_USER="root"
DB_PASS="Varunreddy@123"
DB_NAME="Address_Book_Db"
OUTPUT_PATH="/c/Users/varun/OneDrive/Desktop/GE/AddressBookSystem/src/address_book_report.csv"

REPORT_DATE=$(date '+%Y-%m-%d %H:%M:%S')

TOTAL_BOOKS=$(mysql -h "$DB_HOST" -u "$DB_USER" -p"$DB_PASS" -D "$DB_NAME" --batch --silent -e "SELECT COUNT(*) FROM address_books;")

AVG_CONTACTS=$(mysql -h "$DB_HOST" -u "$DB_USER" -p"$DB_PASS" -D "$DB_NAME" --batch --silent -e "
SELECT ROUND(AVG(contact_count), 2) FROM (
  SELECT COUNT(c.id) AS contact_count
  FROM address_books ab
  LEFT JOIN contacts c ON ab.id = c.address_book_id
  GROUP BY ab.id
) AS counts;")

echo "Report Generated At,Total Address Books,Address Book Name,Total Contacts in Book,Average Contacts per Address Book" > "$OUTPUT_PATH"

mysql -h "$DB_HOST" -u "$DB_USER" -p"$DB_PASS" -D "$DB_NAME" --batch --silent -e "
SELECT
  '$REPORT_DATE' AS report_time,
  '$TOTAL_BOOKS' AS total_books,
  ab.name AS address_book_name,
  COUNT(c.id) AS total_contacts,
  '$AVG_CONTACTS' AS average_contacts
FROM address_books ab
LEFT JOIN contacts c ON ab.id = c.address_book_id
GROUP BY ab.id;" | tr '\t' ',' >> "$OUTPUT_PATH"

echo "Report saved to $OUTPUT_PATH"
