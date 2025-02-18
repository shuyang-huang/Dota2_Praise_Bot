import requests
from config.config import Config


class Stratz:

    stratz_endpoint_url = "https://api.stratz.com/graphql"

    @classmethod
    def get_match_data(cls, match_id: str):
        headers = {
            "Authorization": f"Bearer {Config.stratz_token}",
            "Content-Type": "application/json",
            "User-Agent": "STRATZ_API"
        }
        response = requests.post(cls.stratz_endpoint_url,
                                 json={"query": cls.generate_stratz_request_body(match_id)},
                                 headers=headers)

        if response.status_code != 200:
            # TODO:
            print("❌ 403 Forbidden")
            return ""

        return response.text

    @classmethod
    def generate_stratz_request_body(cls, match_id: str):
        return cls.get_stratz_graphiql_template().replace("<match_id>", match_id)

    @classmethod
    def get_stratz_graphiql_template(cls):
        return """
            query {
                match(id: <match_id>) {
                    id
                    durationSeconds
                    towerStatusDire
                    towerStatusRadiant
                    firstBloodTime
                    averageRank
                    averageImp
                    analysisOutcome
                    radiantNetworthLeads
                    radiantExperienceLeads
                    radiantKills
                    direKills
                        bottomLaneOutcome
                    midLaneOutcome
                    topLaneOutcome
                    players {
                      isRadiant
                      isVictory
                      hero {
                        id
                        displayName
                        aliases
                      }
                      kills
                      deaths
                      assists
                      numLastHits
                      numDenies
                      goldPerMinute
                      networth
                      level
                      experiencePerMinute
                      heroDamage
                      towerDamage
                      heroHealing
                      isRandom
                      lane
                      position
                      intentionalFeeding
                      imp
                      stats {
                        impPerMinute
                        killEvents {
                          time
                          target
                          isSolo
                          isGank
                          isSmoke
                          isTpRecently
                        }
                        deathEvents {
                          time
                          attacker
                          target
                          isWardWalkThrough
                          isBurst
                          isEngagedOnDeath
                          isTracked
                        }
                        assistEvents {
                          time
                          target
                        }
                        wards {
                          time
                          type
                        }
                        itemPurchases {
                          time
                          itemId
                        }
                      }
                    }
                  }
                }
            """