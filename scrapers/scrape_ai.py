#!/usr/bin/env python3

import scrape_common as sc

print('AI')
d = sc.download('https://www.ai.ch/themen/gesundheit-alter-und-soziales/gesundheitsfoerderung-und-praevention/uebertragbare-krankheiten/coronavirus')
sc.timestamp()

# 2020-03-24
"""
  <h2>
      Bestätigte Fälle
  </h2>

  
  <div class="visualClear">Stand 24.03.2020, 10.00 Uhr</div>
<div class="visualClear">
<ul>
<li>8 infizierte Personen</li>
</ul>
</div>
"""

# 2020-03-26
"""
  <h2>
      Anzahl Fälle
  </h2>

  
  <div class="visualClear">Stand 26.03.2020, 18.00 Uhr</div>
<div class="visualClear">
<ul>
<li>11 laborbestätigte Fälle</li>
</ul>
</div>
"""

# 2020-05-06
"""
<h2>
      Anzahl Fälle kumuliert
  </h2>

  
  <div class="visualClear">Stand 06.05.2020, 11.00 Uhr</div>
<div class="visualClear">
<ul>
<li>25 laborbestätigte Fälle</li>
<li>0 Todesfälle</li>
</ul>
</div>
"""

# 2020-06-09
"""
<h2>
      Anzahl Fälle
  </h2>

  
  <div class="visualClear">Stand 9.6.2020, 8.00 Uhr</div>
<div class="visualClear">
<ul>
<li>25 laborbestätigte Fälle (kumuliert)</li>
<li>0 Todesfälle</li>
<li>0 Personen in Isolation (aktuell)</li>
<li>0 Personen in Quarantäne (aktuell)</li>
</ul>
</div>
"""

print("Date and time:", sc.find('>.*Stand (.+ Uhr).*</div>', d))
print("Confirmed cases:", sc.find('<li>.*?([0-9]+)\s*(infizierte Person(en)?|(labor)?bestätigte Fälle).*<\/li>', d))
print("Deaths:", sc.find('<li>.*?([0-9]+)\s*Todesf.+?lle.*<\/li>', d))
print("Isolated:", sc.find('<li>.*?([0-9]+)\*?\s*Personen\s+in\s*Isolation.*<\/li>', d))
# Since 2020-10-15 AI does not publish reliable quarantine/close contact numbers
#quarantined_close_contact = sc.find('<li>.*?([0-9]+)\+?\s*Personen\s+in\s*Quarant.+ne.*enger\s+Kontakt.*<\/li>', d)
#print("Quarantined:", quarantined_close_contact)
quarantined_travel = sc.find('<li>.*?([0-9]+)\+?\s*Personen\s+in\s*Quarant.+ne.*Einreise\s+Risikoland.*<\/li>', d)
print("Quarantined risk area travel:", quarantined_travel)
#print("Quarantined total:", int(quarantined_close_contact) + int(quarantined_travel))

