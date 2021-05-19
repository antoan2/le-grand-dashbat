from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List

import pandas as pd

from app.data_fetch import fetch_dataset
from app.types import DatasetName

Questions: Dict[DatasetName, List[str]] = {
    'transition': [
        'QUXVlc3Rpb246NTc= - Pensez-vous que vos actions en faveur de l\'environnement peuvent vous permettre de faire des économies ?',
        'QUXVlc3Rpb246NTU= - Diriez-vous que vous connaissez les aides et dispositifs qui sont aujourd\'hui proposés par l\'Etat, les collectivités, les entreprises et les associations pour l\'isolation et le chauffage des logements, et pour les déplacements ?',
        'QUXVlc3Rpb246NTg= - Pensez-vous que les taxes sur le diesel et sur l’essence peuvent permettre de modifier les comportements des utilisateurs ?',
        'QUXVlc3Rpb246NjI= - À quoi les recettes liées aux taxes sur le diesel et l’essence doivent-elles avant tout servir ?',
        'QUXVlc3Rpb246NjE= - Selon vous, la transition écologique doit être avant tout financée :',
        'QUXVlc3Rpb246NjA= - Et qui doit être en priorité concerné par le financement de la transition écologique ?',
        'QUXVlc3Rpb246NTk= - Que faudrait-il faire pour protéger la biodiversité et le climat tout en maintenant des activités agricoles et industrielles compétitives par rapport à leurs concurrents étrangers, notamment européens ?',
    ],
    'fiscalite': [
        'QUXVlc3Rpb246NjU= - Afin de réduire le déficit public de la France qui dépense plus qu\'elle ne gagne, pensez-vous qu\'il faut avant tout:',
        'QUXVlc3Rpb246NjQ= - Afin de baisser les impôts et réduire la dette, quelles dépenses publiques faut-il réduire en priorité ?',
        'QUXVlc3Rpb246NjY= - Parmi les dépenses de l\'Etat et des collectivités territoriales, dans quels domaines faut-il faire avant tout des économies ?',
        'QUXVlc3Rpb246Njg= - Seriez-vous prêt à payer un impôt pour encourager des comportements bénéfiques à la collectivité comme la fiscalité écologique ou la fiscalité sur le tabac ou l\'alcool ?',
    ],
    'democratie': [
        'QUXVlc3Rpb246NzI= - Selon vous, faut-il introduire une dose de proportionnelle pour certaines élections, lesquelles ?',
        'QUXVlc3Rpb246NzQ= - Pensez-vous qu\'il serait souhaitable de réduire le nombre de parlementaires (députés + sénateurs = 925) ?',
        'QUXVlc3Rpb246NzY= - Faut-il rendre le vote obligatoire ?',
        'QUXVlc3Rpb246Nzg= - Faut-il avoir davantage recours au référendum au niveau national ?',
        'QUXVlc3Rpb246Nzc= - Faut-il avoir davantage recours au référendum au niveau local ?',
        'QUXVlc3Rpb246ODA= - Faut-il tirer au sort des citoyens non élus pour les associer à la décision publique ?',
        'QUXVlc3Rpb246ODM= - Diriez-vous que l\'application de la laïcité en France est aujourd\'hui:',
    ],
    'organisation': [
        'QUXVlc3Rpb246ODY= - Savez-vous quels sont les différents échelons administratifs (Etat, collectivités territoriales comme la région, la commune, opérateurs comme par exemple Pole Emploi ou la CAF) qui gèrent les différents services publics dans votre territoire ?',
        'QUXVlc3Rpb246ODc= - Pensez-vous qu’il y a trop d’échelons administratifs en France ?',
        'QUXVlc3Rpb246ODU= - Quels sont les niveaux de collectivités territoriales auxquels vous êtes le plus attaché ?',
        'QUXVlc3Rpb246OTA= - Lorsqu\'un déplacement est nécessaire pour effectuer une démarche administrative, quelle distance pouvez-vous parcourir sans difficulté ?',
        'QUXVlc3Rpb246ODk= - Pour accéder à certains services publics, vous avez avant tout des besoins...',
        'QUXVlc3Rpb246OTg= - Si vous rencontrez des difficultés pour effectuer vos démarches administratives sur Internet, de quel accompagnement souhaiteriez-vous bénéficier ?',
        'QUXVlc3Rpb246OTc= - Seriez-vous d\'accord pour qu\'un agent public effectue certaines démarches à votre place ?',
        'QUXVlc3Rpb246OTY= - Que pensez-vous du regroupement dans un même lieu de plusieurs services publics (Maisons de services au public) ?',
        'QUXVlc3Rpb246OTU= - Que pensez-vous des services publics itinérants (bus de services publics) ?',
        'QUXVlc3Rpb246OTQ= - Que pensez-vous du service public sur prise de rendez-vous ?',
        'QUXVlc3Rpb246OTM= - Que pensez-vous des agents publics polyvalents susceptibles de vous accompagner dans l\'accomplissement de plusieurs démarches quelle que soit l\'administration concernée ?',
        'QUXVlc3Rpb246MTA0 - Avez-vous déjà renoncé à des droits / des allocations en raison de démarches administratives trop complexes ?',
    ],
}


def _cleanup_dataset(dataframe: pd.DataFrame) -> pd.DataFrame:
    result = dataframe.copy()
    del result['id']
    del result['createdAt']
    del result['updatedAt']
    result['publishedAt'] = result.publishedAt.apply(datetime.fromisoformat)
    return result


@dataclass
class Dataset:
    name: DatasetName
    questions: List[str] = field(init=False)
    data: pd.DataFrame = field(init=False)

    def __post_init__(self):
        self.data = _cleanup_dataset(fetch_dataset(self.name))
        self.questions = Questions[self.name]
