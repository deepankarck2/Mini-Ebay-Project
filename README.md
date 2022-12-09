# Documentation and Reports
* [Phase-II Report](https://github.com/deepankarck2/Mini-Ebay-Project/files/10088725/X_chakraborty_phase_II.pdf)
## Demo Home Page:

<img src="https://user-images.githubusercontent.com/52084764/203933545-c9dfdf72-c5ba-44d6-8ec3-76c1e9452b17.png" height=780px width=710px>


# An Electronic Trading System aka (Mini-Ebay)
#### We want to develop electronic trading such that every responsible user can trade their items. There are three types of users to this system: 
1. Superusers (SUs), 
2. Ordinary users (OUs),and 
3. Guests (GUs).

## An Super User can perform the tasks below:

- [X] 1.Process applications and decide who can be OU and who should be denied with justifications.
- [X] 2.Process items the OUs submitted intending to sell, some can be publicly available on the system and some may be deniedand communicated to the OU.
- [ ] 3.Send warnings to OUs who received two complaints or the average grade is lower than 2 with at least 3 evaluators, should an OU receive two warnings this OU should be removed from the system automatically.
  - [X] The SU has the power to remove any OU(s) with justifications at any time.
- [ ] 4.Collect transaction statistics for a certain period (a day or a week) and/or a certain OU(s). 
- [ ] 5.Settle disputes between sellers and buyers and apply warnings/removals accordingly.

## An Ordinary users can do the following tasks:
- [X] 1.Features enjoyed by a GU.
- [ ] 2.Deposit or withdraw money (symbolically, no real money is involved in the system) from own account. After a transaction, the buyer’s money is transferred to the seller. A bidder cannot place a bid with amount more than s/he has in the system.
- [ ] 3.Submit the bid to buy an available item, the OU who owns the item however decides if this transaction should proceed.
- [X] 4.Submit the information (a picture or video, title, key words, time limit, price range) of the item(s) s/he wants to sell. 
- [ ] 5.Sell the item(s)s/he posted, the OUmay choose whom to sell, if not the highest bidder was chosen, a reason must be provided.
- [ ] 6.File complaints to SUs against certain OUs whose item s/he purchased has some problem.
- [X] 7.Grade an OU after buying an item from him/her, 1 being the worst and 5 being the best. 
  - [ ] 7.1 Any OU making 3 1 (worst) or 5(best) rating to others, the OU must see the SU to make sure there is no problem, a warning or removal could ensure based on SU’s judgment.
- [ ] 8.See his/her own transaction history.
- [ ] 9.Change his/her password, name, address, phone,and credit card number.


## A GU can do the following tasks:
- [X] 1.Browse/search available items based on title, keywords, price range, and ratings; 
- [X] 2.Report to SU about the suspicious items (stolen) s/he spot from the site, if proven true the SU will remove the item and the CU who posted it and generate a report to be sent to police;
- [X] 3.Apply to be an OU

## Other system constraints:

- [ ] 1.OUs removed from the system by SUs will be blocked for future re-application.
- [ ] 2.Items removed from the systemby SUs will be blacklisted fromsystem.
- [ ] 3.The system can distinguish the interest of an OU during the login session and show different GUI according to the users’ browsing or selling/buying history. No adaptive GUI for GUs or SUs.
- [ ] 4.GUI is required, could be a local application or web-based one, no preference
- [ ] 5.A creative feature with 10% of the project determined by each team, considerably creative ones (positive outliers) could obtain special bonus.
