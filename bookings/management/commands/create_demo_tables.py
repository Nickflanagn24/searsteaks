from django.core.management.base import BaseCommand
from bookings.models import Table

class Command(BaseCommand):
    help = 'Creates demo tables for testing'

    def handle(self, *args, **options):
        # Check existing tables
        existing_count = Table.objects.count()
        self.stdout.write(f"Found {existing_count} existing tables")
        
        # Create tables
        tables_to_create = 10 - existing_count
        if tables_to_create <= 0:
            self.stdout.write(self.style.SUCCESS('No tables need to be created'))
            return
        
        for i in range(1, tables_to_create + 1):
            table_number = existing_count + i
            capacity = 2 if i % 3 == 0 else 4  # Mix of 2 and 4 seat tables
            
            Table.objects.create(
                table_number=table_number,
                capacity=capacity,
                is_available=True
            )
            self.stdout.write(f"Created table {table_number} with capacity {capacity}")
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created {tables_to_create} demo tables'))
