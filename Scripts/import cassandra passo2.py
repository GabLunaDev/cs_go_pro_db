from cassandra.cluster import Cluster
import mysql.connector

# Connect to Cassandra
cluster = Cluster(['127.0.0.1'])  # Replace with your Cassandra cluster address
session = cluster.connect('cs_go')  # Assuming your keyspace is named 'cs_go'

# Connect to MySQL
mysql_connection = mysql.connector.connect(
    host="localhost",  # Replace with your MySQL host
    user="root",  # Replace with your MySQL username
    password="12345678",  # Replace with your MySQL password
    database="csgo_players"  # Replace with your MySQL database name
)
mysql_cursor = mysql_connection.cursor(dictionary=True)


# Define function to fetch data from MySQL and insert into Cassandra
def transfer_data(mysql_table, cassandra_fields):
    mysql_cursor.execute(f"SELECT * FROM {mysql_table}")
    rows = mysql_cursor.fetchall()
    for row in rows:
        cassandra_fields_str = ', '.join(cassandra_fields)
        placeholders = ', '.join(['%s'] * len(cassandra_fields))

        # Modify this part for the 'teams' column
        if 'teams' in row:
            teams_set = set(row['teams'].split(', '))
        else:
            teams_set = set()  # If 'teams' column doesn't exist, initialize an empty set

        session.execute(f"""
            INSERT INTO player_info ({cassandra_fields_str})
            VALUES ({placeholders})
        """, tuple(row[field] if field != 'teams' else teams_set for field in cassandra_fields))


# Transfer data from MySQL to Cassandra
transfer_data('player', ['player_id', 'nickname', 'real_name', 'age', 'country'])
transfer_data('team', ['player_id', 'current_team', 'teams'])
transfer_data('p_stat', ['player_id', 'total_kills', 'total_deaths', 'headshot_percentage',
                         'maps_played', 'rounds_played', 'kills_to_death_diff',
                         'total_opening_kills', 'total_opening_deaths', 'opening_kill_ratio',
                         'opening_kill_rating', 'first_kill_won_rounds', 'rating'])
transfer_data('weapon_stat', ['player_id', 'rifle_kills', 'sniper_kills', 'smg_kills',
                              'pistol_kills', 'grenade_kills', 'other_kills'])
transfer_data('round_stat', ['player_id', 'damage_per_round', 'grenade_dmg_per_round',
                             'kills_per_round', 'assists_per_round', 'deaths_per_round',
                             'saved_by_teammate_per_round', 'saved_teammates_per_round',
                             'rounds_with_kills', 'team_win_percent_after_first_kill',
                             'zero_kill_rounds', 'one_kill_rounds', 'two_kill_rounds',
                             'three_kill_rounds', 'four_kill_rounds', 'five_kill_rounds'])

# Close connections
mysql_cursor.close()
mysql_connection.close()
cluster.shutdown()