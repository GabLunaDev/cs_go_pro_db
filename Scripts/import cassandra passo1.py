from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'], port = 9042)  # Replace with your Cassandra cluster address
session = cluster.connect()

########################## CREATE KEYSPACE DO CSGO ################################
session.execute("""
    CREATE KEYSPACE IF NOT EXISTS cs_go_new2
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}
""")
session.set_keyspace('cs_go_new2')

#################### CRIANDO NOSSA TABLE PLAYERINFO DENTRO DO CONTAINER  #######################
session.execute("""
    CREATE TABLE IF NOT EXISTS player_info (
        player_id INT PRIMARY KEY,
        nickname VARCHAR,
        real_name VARCHAR,
        age INT,
        country VARCHAR,
        current_team VARCHAR,
        teams SET<VARCHAR>,
        total_kills INT,
        total_deaths INT,
        headshot_percentage DOUBLE,
        maps_played INT,
        rounds_played INT,
        kills_to_death_diff VARCHAR,
        total_opening_kills INT,
        total_opening_deaths INT,
        opening_kill_ratio DOUBLE,
        opening_kill_rating DOUBLE,
        first_kill_in_won_rounds DOUBLE,
        rating DOUBLE,
        rifle_kills INT,
        sniper_kills INT,
        smg_kills INT,
        pistol_kills INT,
        grenade_kills INT,
        other_kills INT,
        damage_per_round DOUBLE,
        grenade_dmg_per_round DOUBLE,
        kills_per_round DOUBLE,
        assists_per_round DOUBLE,
        deaths_per_round DOUBLE,
        saved_by_teammate_per_round INT,
        saved_teammates_per_round INT,
        rounds_with_kills DOUBLE,
        team_win_percent_after_first_kill DOUBLE,
        zero_kill_rounds INT,
        one_kill_rounds INT,
        two_kill_rounds INT,
        three_kill_rounds INT,
        four_kill_rounds INT,
        five_kill_rounds INT
    )
""")


cluster.shutdown()