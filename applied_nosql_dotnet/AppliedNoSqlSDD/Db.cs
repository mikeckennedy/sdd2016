using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;
using MongoDB.Driver;

namespace AppliedNoSqlSDD
{
	class Db
	{
		public IMongoDatabase db;

		public Db()
		{
			var client = new MongoClient();
			this.db = client.GetDatabase("sdd_blog");
		}

		public IMongoCollection<Post> Posts
		{
			get { return db.GetCollection<Post>("Post"); }
		}

		public IMongoCollection<User> Users
		{
			get { return db.GetCollection<User>("User"); }
		}
	}

	[BsonIgnoreExtraElements]
	class Post// : ISupportInitialize
	{
		public ObjectId Id { get; set; }
		public string Title { get; set; }
		public DateTime Published { get; set; }
		public string Url { get; set; }
		public List<Comment> Comments { get; set; }

		public string PublishedText { get; set; }

		public Post()
		{
			this.Published = DateTime.Now;
			this.Comments = new List<Comment>();
		}
	}

	struct Comment
	{
		public string Name { get; set; }
		public DateTime Created { get; set; }
		public string CommentText { get; set; }

		//public Comment()
		//{
		//	this.Created = DateTime.Now;
		//}
	}

	class User
	{
		public string Id { get; set; }
		public string Name { get; set; }

		public User()
		{
			Id = Guid.NewGuid().ToString("N");
		}
	}
}
