create database csgo_players;

use csgo_players;

CREATE TABLE player (
    player_id INT PRIMARY KEY,
    nickname varchar(500),
    real_name varchar(500),
    age INT,
    country varchar(500)
    );

CREATE TABLE IF NOT EXISTS team (
    player_id INT,
    current_team varchar(500),
    teams varchar(500),
    foreign key (player_id) references player(player_id)
);



CREATE TABLE IF NOT EXISTS p_stat (
    player_id INT ,
    total_kills INT,
    total_deaths INT,
    headshot_percentage DOUBLE,
    maps_played INT,
    rounds_played INT,
    kills_to_death_diff varchar(500),
    total_opening_kills INT,
    total_opening_deaths INT,
    opening_kill_ratio DOUBLE,
    opening_kill_rating DOUBLE,
    first_kill_in_won_rounds DOUBLE,
    rating DOUBLE,
    foreign key (player_id) references player(player_id)
);

CREATE TABLE IF NOT EXISTS weapon_stat (
    player_id INT ,
    rifle_kills INT,
    sniper_kills INT,
    smg_kills INT,
    pistol_kills INT,
    grenade_kills INT,
    other_kills INT,
    foreign key (player_id) references player(player_id)
);

CREATE TABLE IF NOT EXISTS round_stat (
    player_id INT ,
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
    five_kill_rounds INT, 
    FOREIGN KEY (player_id) REFERENCES player(player_id)
);




