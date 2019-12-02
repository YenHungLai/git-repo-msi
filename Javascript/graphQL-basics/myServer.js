const express = require('express');
const expressGraphQL = require('express-graphql');
const {
	GraphQLSchema,
	GraphQLObjectType,
	GraphQLString,
	GraphQLInt,
	GraphQLList,
	GraphQLNonNull
} = require('graphql');

const app = express();

const contacts = [
	{ name: 'Jacob', phoneNumber: 1234123 },
	{ name: 'Joy', phoneNumber: 3241412 },
	{ name: 'Jsoh', phoneNumber: 2342341 },
	{ name: 'Nick', phoneNumber: 12312312 }
];

const phones = [
	{ owner: 'Jacob', phone: 'Samsung' },
	{ owner: 'Joy', phone: 'Iphone' },
	{ owner: 'Jsoh', phone: 'XiaoMi' },
	{ owner: 'Nick', phone: 'HTC' }
];

const ContactType = new GraphQLObjectType({
	name: 'Contact',
	description: 'A single contact',
	fields: () => ({
		name: { type: GraphQLString },
		phoneNumber: { type: GraphQLInt },
		phone: {
			type: PhoneType,
			resolve: contact =>
				phones.find(phone => phone.owner === contact.name)
		}
	})
});

const PhoneType = new GraphQLObjectType({
	name: 'Phone',
	description: 'A single Phone',
	fields: () => ({
		owner: { type: GraphQLString },
		phone: { type: GraphQLString }
	})
});

const RootQueryType = new GraphQLObjectType({
	name: 'Root',
	description: 'Root of my query',
	fields: () => ({
		contacts: {
			type: GraphQLList(ContactType),
			description: 'List of contacts',
			resolve: () => contacts
		}
	})
});

const schema = new GraphQLSchema({
	query: RootQueryType
});

app.use(
	'/graphql',
	expressGraphQL({
		schema,
		graphiql: true
	})
);

app.listen(3000, console.log('Server running on port 3000'));
