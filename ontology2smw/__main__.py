import sys
from ontology2smw.cli_args import parser
from ontology2smw.functions import writetowiki_decision
from ontology2smw.functions import sparql2smwpage

args = parser.parse_args()


def main():
    if not args.ontology:
        print("Error: mandatory argument --ontology was not provided",
              file=sys.stderr)
        sys.exit()
    if args.write:
        writetowiki_decision()

    sparql2smwpage(
        sparql_fn='ontology2smw/queries/query_classes_properties.rq',
        format_=args.format,
        source=args.ontology,
    )


if __name__ == '__main__':
    main()
