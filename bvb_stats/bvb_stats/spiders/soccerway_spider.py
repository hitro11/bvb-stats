import scrapy


class SoccerwaySpider(scrapy.Spider):
    name = "soccerway"
    start_urls = [
        'https://www.soccerway.com/national/germany/bundesliga/20182019/regular-season/r47657/',
        'https://www.soccerway.com/teams/germany/bv-borussia-09-dortmund/964/',
    ]

    def parse(self, response):
        
        if response.request.url == 'https://www.soccerway.com/national/germany/bundesliga/20182019/regular-season/r47657/':
            leagueStandings = response.xpath('//*[@id="page_competition_1_block_competition_tables_7"]').extract_first()
            leagueStandings = leagueStandings.encode('utf-8').strip()
            filename = 'standings.html'
            with open(filename, 'wb') as f:
                f.write(leagueStandings)
                f.close()
      
        if response.request.url == 'https://www.soccerway.com/teams/germany/bv-borussia-09-dortmund/964/':
            fixtures = response.xpath('//*[@id="page_team_1_block_team_matches_summary_7"]').extract_first()
            fixtures = fixtures.encode('utf-8').strip()
            filename = 'fixtures.html'
            with open(filename, 'wb') as f:
                f.write(fixtures)
                f.close()
            