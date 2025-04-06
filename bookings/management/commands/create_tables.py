from django.core.management.base import BaseCommand
from bookings.models import Table

class Command(BaseCommand):
    help = 'Creates demo tables for the restaurant'

    def handle(self, *args, **options):
        # Check if tables already exist
        existing_count = Table.objects.count()
        self.stdout.write(f"Found {existing_count} existing tables")
        
        if existing_count >= 8:
            self.stdout.write(self.style.SUCCESS('Sufficient tables already exist'))
            return
        
        # Define tables to create
        tables_to_create = [
            {"number": 1, "capacity": 2},
            {"number": 2, "capacity": 4},
            {"number": 3, "capacity": 2},
            {"number": 4, "capacity": 6},
            {"number": 5, "capacity": 4},
            {"number": 6, "capacity": 8},
            {"number": 7, "capacity": 2},
            {"number": 8, "capacity": 4},
        ]
        
        # Create tables (skipping any that already exist by table number)
        existing_numbers = Table.objects.values_list('table_number', flat=True)
        created_count = 0
        
        for table_data in tables_to_create:
            if table_data["number"] not in existing_numbers:
                Table.objects.create(
                    table_number=table_data["number"],
                    capacity=table_data["capacity"],
                    is_available=True
                )
                created_count += 1
                self.stdout.write(f"Created Table {table_data['number']} with capacity {table_data['capacity']}")
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created {created_count} new tables'))
